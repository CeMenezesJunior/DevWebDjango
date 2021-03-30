from django.urls import path

from album import views

app_name = 'album'
urlpatterns = [
    path('<int:id>/<slug:slug_do_album>', views.index, name='albumdetail')
]