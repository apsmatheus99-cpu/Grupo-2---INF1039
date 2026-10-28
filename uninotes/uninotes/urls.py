"""
URL configuration for uninotes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from uninotesapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', cadastro_usuario, name='cadastro_usuario'),
    path('users/',
        include('django.contrib.auth.urls')),
    path('login/', login, name='login'),
    path('login_usuario/', login_usuario, name='login_usuario'),
    path('logout_usuario/', logout_usuario, name='logout_usuario'),
    path('cadastro/', cadastro, name='cadastro'),
    path('perfil/', perfil, name='perfil'),
    path('configuracoes/', configuracoes, name = 'configuracoes'),
    path('estatisticas/', estatisticas, name = 'estatisticas'),
    path('mensagens/', mensagens, name = 'mensagens'),
    path('salvos/', salvos, name= 'salvos'),
    path('materiais/', meus_materiais, name = 'meus_materiais'),

    
    path('material/', material),
    path('mensagens/', mensagens),
    path('esqueci-senha/',esqueci_senha),
    path('', login),
    path('inicio/', inicio, name='inicio'),
    path('publicar/', publicar),

]
