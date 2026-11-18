from django.shortcuts import render, get_object_or_404
from .models import Curso, Faculdade
from django.shortcuts import redirect, render 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as fazer_login, logout as fazer_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Material, Avaliacao
from django.db.models import Avg, Count

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
    material_atual = get_object_or_404(Material, pk=material_id)

    if request.method == 'POST' and 'nota' in request.POST:
        if not request.user.is_authenticated:
            return redirect('login')
        
        nota = request.POST['nota']

        if nota not in ('1', '2', '3', '4', '5'):
            messages.error(request, 'A nota precisa ser de 1 a 5.')
            return redirect(request.path)

        Avaliacao.objects.update_or_create(
            material=material_atual,
            usuario=request.user,
            defaults={'avaliacao': int(nota)},
        )

        return redirect(request.path)
        



    resumo = material_atual.avaliacoes.filter(
        usuario__isnull=False,
        avaliacao__range=(1, 5),
    ).aggregate(
        media=Avg('avaliacao'),
        quantidade=Count('id'),
    )

    return render(request, 'material.html', {
        'material': material_atual,
        'media_avaliacoes': resumo['media'],
        'quantidade_avaliacoes': resumo['quantidade'],
    })


def mensagens(request):
    return render(request,'tela_mensagem.html')
    
def esqueci_senha(request):
    return render(request, 'esqueci_senha.html')

@login_required(login_url='login')
def inicio(request):
    return render(request, 'telaInicio.html')

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
