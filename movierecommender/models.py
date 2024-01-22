from django.db import models


class Movie(models.Model):
    """
    Django Movie Model
    """
    imdb_id = models.CharField(max_length=48, null=False)           # IMDB id
    genres = models.CharField(max_length=200, null=True)            # Movie genres
    original_language = models.CharField(max_length=20, null=True)  # Original language
    original_title = models.CharField(max_length=500, null=False)   # Original movie title
    release_date = models.IntegerField(default=1970)                # Movie release date
    overview = models.TextField(max_length=2000, null=True)         # Movie overview
    vote_average = models.FloatField(default=0)                     # Average voting for the movie
    vote_count = models.IntegerField(default=0)                     # Total votes for ths movie
    poster_path = models.CharField(max_length=64, null=True)        # The movie's poster path
    watched = models.BooleanField(default=False, null=True)         # If you have watched this movie
    recommended = models.BooleanField(default=False, null=True)     # If this movie will be recommended
