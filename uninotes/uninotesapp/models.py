from django.db import models

class Curso(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Faculdade(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Aluno(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Avaliacao(models.Model):
    ESTRELAS = [
            (0, 'Sem avaliação'),
            (1, '⭐'),
            (2, '⭐⭐'),
            (3, '⭐⭐⭐'),
            (4, '⭐⭐⭐⭐'),
            (5, '⭐⭐⭐⭐⭐'),
        ]   
    avaliacao = models.IntegerField( default=0, choices= ESTRELAS)
    material = models.ForeignKey('Material',on_delete=models.CASCADE,related_name='avaliacoes')
    
    def __str__(self):
        return str(self.avaliacao)    

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
    professor = models.ForeignKey(Professor,on_delete=models.PROTECT,null=True,blank=True)
    arquivo = models.FileField(upload_to='materiais/')
    data_publicacao = models.DateTimeField(auto_now_add=True)
    comentarios = models.TextField(blank=True)
    

    def __str__(self):
        return self.titulo

class Materiais_salvos(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name = 'Meus_materiais')
    material = models.ForeignKey(Material, on_delete= models.CASCADE, related_name = 'publicacoes')
    visualizacoes = models.PositiveIntegerField(default=0)
    downloads = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.material.titulo



