from django.shortcuts import render

def login(request):
    return render(request, 'tela_login.html')

def cadastro(request):
    return render(request, 'tela_cadastro.html')

def material(request):
    return render(request,'material.html')

def mensagens(request):
    return render(request,'tela_mensagem.html')