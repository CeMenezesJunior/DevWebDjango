from django.shortcuts import render

def index(request,id,slug_do_album):
    frase="Tela de albuns"
    return render(request,'album/index.html',{'frase':frase})