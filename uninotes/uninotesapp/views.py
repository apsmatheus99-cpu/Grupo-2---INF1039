from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as fazer_login, logout as fazer_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Curso, Denuncia, Faculdade, Material, Comentario, Mensagem
from django.urls import reverse


def login(request):
    return render(request, 'tela_login.html')

def cadastro(request):
    cursos = Curso.objects.all()
    faculdades = Faculdade.objects.all()

    return render(request, 'tela_cadastro.html',{
        'cursos': cursos,
        'faculdades': faculdades
    })

@login_required(login_url='login')
def material(request, material_id):
    material = get_object_or_404(
        Material.objects.select_related(
            'curso',
            'faculdade',
            'professor',
            'usuario'
        ),
        id=material_id
    )

    return render(request, 'material.html', {'material': material})

@login_required(login_url='login')
def mensagens(request):
    if request.method== 'POST':
        destinatario_id= request.POST.get('destinatario')
        conteudo= request.POST.get('conteudo', '').strip()
        if destinatario_id and conteudo:
            destinatario = get_object_or_404(User, id=destinatario_id)
            Mensagem.objects.create(remetente= request.user, destinatario= destinatario, conteudo= conteudo)
        return redirect(f"{reverse('mensagens')}?contato={destinatario_id}")
    contato_id= request.GET.get('contato')
    print("id dos contatos: ", contato_id) #lembrar de remover depois
    contato_selecionado= None
    mensagens_conversa=[]
    if contato_id:
        contato_selecionado= get_object_or_404(User, id= contato_id)
        if contato_selecionado:
            mensagens_enviadas= Mensagem.objects.filter(remetente= request.user, destinatario= contato_selecionado)
            mensagens_recebidas= Mensagem.objects.filter(remetente= contato_selecionado, destinatario= request.user)
            print("mensagens enviadas: ", mensagens_enviadas) #lembrar de remover depois
            print("mensagens recebidas: ", mensagens_recebidas) #lembrar de remover depois
            mensagens_conversa= (mensagens_enviadas | mensagens_recebidas).order_by('data_envio')
            print("historico: ", mensagens_conversa) #lembrar de remover depois
    contatos= User.objects.exclude(id=request.user.id)
    return render(request, 'tela_mensagem.html', {'contatos': contatos, 'contato_selecionado': contato_selecionado, 'mensagens_conversa': mensagens_conversa})

    
def esqueci_senha(request):
    return render(request, 'esqueci_senha.html')

@login_required(login_url='login')
def inicio(request):
    materiais = Material.objects.all()

    return render(request, 'telaInicio.html', {
        'materiais': materiais
    })

@login_required(login_url='login')
def configuracoes(request):
    return render(request, 'pagina_configuracoes.html')

@login_required(login_url='login')
def perfil(request):
    return render(request, 'tela_de_perfil.html')

@login_required(login_url='login')
def estatisticas(request):
    return render(request, 'tela_estatistica.html')

@login_required(login_url='login')
def meus_materiais(request):
    return render(request, 'meus materiais.html')

@login_required(login_url='login')
def salvos(request):
    return render(request, 'salvos.html')

@login_required(login_url='login')
def publicar(request):
    return render(request, 'pagina de publica.html')

def login_usuario(request):
    if request.method == "POST":
        email = request.POST["username"]
        usuario = User.objects.filter(email=email).first()

        if usuario:
            user = authenticate(
                request,
                username=usuario.username,
                password=request.POST["password"]
            )

            if user is not None:
                fazer_login(request, user)
                return redirect("inicio")
            
        messages.error(request, "E-mail ou senha incorretos.")

    return render(request, "tela_login.html")

def logout_usuario(request):
    if request.method == "POST":
        fazer_logout(request)
        return redirect("login")
    
    return redirect("login")        


def cadastro_usuario(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password != confirmpassword:
            messages.error(request, "As senhas não coincidem.")
            return redirect("cadastro")

        user = User.objects.create_user(
            request.POST['name'],
            request.POST['email'], 
            request.POST['password'])

        user.save()
        return redirect("login")
    return render(request, "tela_cadastro.html")

@login_required
@require_POST
def criar_comentario(request, material_id):

    material = get_object_or_404(Material, id=material_id)

    texto = request.POST.get("texto", "").strip()

    if not texto:
        return JsonResponse(
            {"erro": "O comentário não pode estar vazio."},
            status=400
        )

    if len(texto) > 1000:
        return JsonResponse(
            {"erro": "O comentário deve ter no máximo 1000 caracteres."},
            status=400
        )

    comentario = Comentario.objects.create(
        material=material,
        usuario=request.user,
        texto=texto
    )

    nome_usuario = (
        request.user.get_full_name()
        or request.user.username
    )

    return JsonResponse({
        "id": comentario.id,
        "usuario": nome_usuario,
        "texto": comentario.texto
    }, status=201)



@login_required
def salvar_denuncia(request):
    if request.method == "POST":
        descricao = request.POST.get("descricao", "").strip()
        material_id = request.POST.get("material_id")

        if descricao and material_id:
            material = get_object_or_404(Material, pk=material_id)

            Denuncia.objects.create(usuario=request.user,material=material,descricao=descricao)
        return redirect(request.META.get("HTTP_REFERER", "/"))

    return redirect("/")