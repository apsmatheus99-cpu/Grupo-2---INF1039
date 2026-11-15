from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as fazer_login, logout as fazer_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Curso, Faculdade, Material, Comentario

def login(request):
    return render(request, 'tela_login.html')

def cadastro(request):
    cursos = Curso.objects.all()
    faculdades = Faculdade.objects.all()

    return render(request, 'tela_cadastro.html',{
        'cursos': cursos,
        'faculdades': faculdades
    })

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

def mensagens(request):
    return render(request,'tela_mensagem.html')
    
def esqueci_senha(request):
    return render(request, 'esqueci_senha.html')

@login_required(login_url='login')
def inicio(request):
    materiais = Material.objects.all()

    return render(request, 'telaInicio.html', {
        'materiais': materiais
    })

def configuracoes(request):
    return render(request, 'pagina_configuracoes.html')

def perfil(request):
    return render(request, 'tela_de_perfil.html')

def mensagens(request):
    return render(request, 'tela_mensagem.html')

def estatisticas(request):
    return render(request, 'tela_estatistica.html')

def meus_materiais(request):
    return render(request, 'meus materiais.html')

def salvos(request):
    return render(request, 'salvos.html')

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
