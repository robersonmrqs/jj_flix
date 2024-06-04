from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


LISTA_CATEGORIAS = (('JOCA', 'Joca'),
                    ('JUAN', 'Juan'),
                    ('EMDUPLA', 'Em Dupla'),
                    ('ESCOLA', 'Na escola'),
                    ('EXTRAS', 'Extras'))

class Video(models.Model):
    titulo = models.CharField(max_length = 50)
    thumb = models.ImageField(upload_to = 'thumb_videos')
    descricao = models.TextField(max_length = 200)
    categoria = models.CharField(max_length = 10, choices = LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default = 0)
    data_criacao = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.titulo

class Episodio(models.Model):
    filme = models.ForeignKey('Video', related_name = 'episodios', on_delete = models.CASCADE)
    titulo = models.CharField(max_length = 100)
    video = models.FileField(upload_to = 'videos')

    def __str__(self):
        return self.filme.titulo + " - " + self.titulo

class Usuario(AbstractUser):
    videos_vistos = models.ManyToManyField('Video')