from django.db import models

class Album(models.Model):
    album_title =  models.CharField(max_length=500)
    artist = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    released_year = models.CharField(max_length=5, default='-')
    album_logo = models.CharField(max_length=2000)

    def __str__(self):
        return  self.album_title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey( Album , on_delete=models.CASCADE)
    song_title =  models.CharField(max_length=500)
    file_type =  models.CharField(max_length=20)
    is_favourite = models.BooleanField(default = False)

    def __str__(self):
        return  self.song_title

