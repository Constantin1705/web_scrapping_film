from django.db import models

class Movie(models.Model):
    genre_choices = (('comedy', 'Comedy'), ('scifi', 'Scifi'), ('action', 'Action'))

    movie_name = models.CharField(max_length=30)

    genre = models.CharField(max_length=30, choices=genre_choices)
    score = models.CharField(max_length=10)

    # campuri auxiliare
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.movie_name}"



