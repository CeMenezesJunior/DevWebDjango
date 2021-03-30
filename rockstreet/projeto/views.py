from django.shortcuts import render

from album.models import Album
from artista.models import Artista


def index(request):
    lista_de_albuns = Album.objects.all().order_by('nome',)
    lista_de_artistas = Artista.objects.all().order_by('nome',)
    return render(request, 'index.html', {'albuns': lista_de_albuns, 'artistas':lista_de_artistas})

