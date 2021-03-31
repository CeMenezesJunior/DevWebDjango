from django.urls import path

from musica import views
app_name='musica'
urlpatterns = [
    path('<int:id>/<slug:slug_da_musica>',views.index,name='musicadetail')
]