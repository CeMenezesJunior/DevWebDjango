from django.urls import path

from artista import views

app_name='artista'
urlpatterns = [
    path('<int:id>/<slug:slug_do_artista>',views.index,name='artistadetail')
]