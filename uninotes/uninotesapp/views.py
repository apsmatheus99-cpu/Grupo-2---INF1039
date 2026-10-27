from django.shortcuts import render
from .models import Curso
from django.shortcuts import redirect, render 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as fazer_login, logout as fazer_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login(request):
    return render(request, 'tela_login.html')

def cadastro(request):
    return render(request, 'tela_cadastro.html')

def material(request):
    return render(request,'material.html')
    
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
    if request.method=="POST":
        user= authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"]
            )
        if user is not None:
            fazer_login(request, user)
            return redirect("inicio")
        else:
            messages.error(request, "Nome de usuário ou senha incorretos.")
            return render(request, "tela_login.html")
        
    return render(request, "tela_login.html")

def logout_usuario(request):
    if request.method == "POST":
        fazer_logout(request)
        return redirect("login")
    
    return redirect("login")        


