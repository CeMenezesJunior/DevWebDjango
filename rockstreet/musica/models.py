from django.db import models
from django.urls import reverse

from album.models import Album


class Musica(models.Model):
    album = models.ForeignKey(Album,related_name='musicas',on_delete=models.DO_NOTHING)
    num = models.IntegerField()
    nome = models.CharField(max_length=100,db_index=True)
    tempo = models.CharField(max_length=5)
    link = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150)

    class Meta:
        db_table = "musica"
        ordering = ('num',)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('musica:musicadetail',args=[self.id,self.slug])
