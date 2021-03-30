from django.shortcuts import render

from artista.models import Artista


def index(request,id,slug_do_artista):
    artista = Artista.objects.get(id=id,slug=slug_do_artista)
    return render(request,'artista/artista.html',{'artista':artista})
