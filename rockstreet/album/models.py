from django.db import models
from django.urls import reverse

from artista.models import Artista


class Album(models.Model):
    artista = models.ForeignKey(Artista,related_name='albuns',on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=70,db_index=True,unique=True)
    capa = models.CharField(max_length=150)
    link_spotify = models.CharField(max_length=100)
    slug = models.SlugField(max_length=70)

    class Meta:
        db_table="album"
        ordering = ('nome',)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('album:albumdetail',args=[self.id,self.slug])