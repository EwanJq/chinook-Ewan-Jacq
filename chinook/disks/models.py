from django.db import models

class Artist(models.Model):
    #Django gere lui meme les idées selon les assignations avec des clés etrangères
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    #Album possede une clé etrangère vers artist : models.ForeignKey(vers, si l'objet est supprimé, nom de relation
    #Le nom de relation sert à donner les albums liés à l'artiste : artist.albums.all()

    def __str__(self):
        return f"{self.title} ({self.artist.name})"


class Track(models.Model):
    name = models.CharField(max_length=100, null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
    milliseconds = models.IntegerField(help_text="Duration in milliseconds")
    composer = models.CharField(max_length=100, null=True)
    bytes = models.IntegerField()
    unitPrice = models.FloatField()
    
    def __str__(self):
        return f"{self.name} - {self.album.title} ({self.milliseconds} ms)"

