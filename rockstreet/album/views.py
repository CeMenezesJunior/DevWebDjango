from django.shortcuts import render

from album.models import Album


def index(request,id,slug_do_album):
    album = Album.objects.get(id=id,slug=slug_do_album)
    return render(request,'album/album.html',{'album':album})