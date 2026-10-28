from django.contrib import admin
from .models import Curso, Faculdade, Material, Professor, Aluno, Avaliacao, Materiais_salvos

admin.site.register(Curso)
admin.site.register(Faculdade)
admin.site.register(Material)
admin.site.register(Professor)
admin.site.register(Aluno)
admin.site.register(Avaliacao)
admin.site.register(Materiais_salvos)

