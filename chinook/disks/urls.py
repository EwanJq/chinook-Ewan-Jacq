from django.urls import path
from . import views  # Importation des vues


app_name = "disks"
urlpatterns = [
    path("albums", views.album_list, name="albums"),

]