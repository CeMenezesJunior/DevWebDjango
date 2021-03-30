from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=70, db_index=True, unique=True)
    descricao = models.CharField(max_length=100)
    imagem = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=70)

    class Meta:
        db_table='artista'
        ordering = ('nome',)

    def __str__(self):
        return self.nome
