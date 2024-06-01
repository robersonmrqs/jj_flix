from django.db import models
from django.utils import timezone

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