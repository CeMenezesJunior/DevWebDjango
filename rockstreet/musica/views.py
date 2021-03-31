from django.shortcuts import render

from musica.models import Musica



def index(request,id,slug_da_musica):
    musica = Musica.objects.get(id=id,slug=slug_da_musica)
    return render(request,'musica/musica.html',{'musica':musica})