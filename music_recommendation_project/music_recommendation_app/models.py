from django.db import models

class Music(models.Model):
    name = models.CharField(max_length=255)
    artists = models.CharField(max_length=255)
    year = models.IntegerField()
    valence = models.FloatField()
    acousticness = models.FloatField()
    danceability = models.FloatField()
    duration_ms = models.FloatField()
    energy = models.FloatField()
    explicit = models.FloatField()
    instrumentalness = models.FloatField()
    key = models.FloatField()
    liveness = models.FloatField()
    loudness = models.FloatField()
    mode = models.FloatField()
    popularity = models.FloatField()
    speechiness = models.FloatField()
    tempo = models.FloatField()

    def __str__(self):
        return self.name

class Recommendation(models.Model):
    seed_songs = models.TextField()
    recommended_songs = models.TextField()

    def __str__(self):
        return f"Recommendation for {self.seed_songs}"