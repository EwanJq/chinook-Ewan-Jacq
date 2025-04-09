from django.shortcuts import render
from .models import Album # obligé pour faire le getters !

def album_list(request):
    albums = Album.objects.select_related('artist').all()  # optimisé pour DB
    return render(request, 'disks/albums.html', {'albums': albums})