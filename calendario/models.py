from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateField()
    cor = models.CharField(max_length=20)

    def __str__(self):
        return self.titulo