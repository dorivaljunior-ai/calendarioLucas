from django.db import models


class Tag(models.Model):
    nome = models.CharField(max_length=100)
    cor = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateField()
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo