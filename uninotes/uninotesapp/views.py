from django.shortcuts import render
from .models import Curso

def login(request):
    return render(request, 'tela_login.html')

def cadastro(request):
    return render(request, 'tela_cadastro.html')

def material(request):
    return render(request,'material.html')
def esqueci_senha(request):
    return render(request, 'esqueci_senha.html')

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
