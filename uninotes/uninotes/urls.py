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
from django.contrib.auth import views
from django.urls import path, include
from uninotesapp.views import *
from django.conf import settings
from django.conf.urls.static import static
from uninotesapp import views as app_views


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

    path('material/<int:material_id>/', material, name='material'),
    path('esqueci-senha/',esqueci_senha),
    path('', login),
    path('inicio/', inicio, name='inicio'),
    path('publicar/', publicar, name='publicar'),
    path(
        "material/<int:material_id>/comentarios/",
        criar_comentario,
        name="criar_comentario"
    ),
    path("salvar-denuncia/", salvar_denuncia, name="salvar_denuncia"),
    path('material/<int:material_id>/denuncia/',app_views.modal_denuncia,name='modal_denuncia'),
    path('material/<int:material_id>/baixar/',app_views.baixar_material,name='baixar_material'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
