from django.shortcuts import render

def login(request):
    return render(request, 'tela_login.html')

def cadastro(request):
    return render(request, 'tela_cadastro.html')

def esqueci_senha(request):
    return render(request, 'esqueci_senha.html')

def inicio(request):
    return render(request, 'telaInicio.html')