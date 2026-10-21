from django.db import models

class Curso(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Faculdade(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Material(models.Model):
    titulo = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=100)

    TIPOS = [
        ('txt', 'Texto'),
        ('exerc', 'Exercício'),
        ('pr', 'Prova'),
        ('slide', 'Slide'),
        ('anot', 'Anotação'),
        ('resumo', 'Resumo'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPOS)

    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    faculdade = models.ForeignKey(Faculdade, on_delete=models.PROTECT)

    professor = models.CharField(max_length=100, blank=True)
    descricao = models.TextField()
    tags = models.CharField(max_length=200, blank=True)
    arquivo = models.FileField(upload_to='materiais/')
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo