from django.db import models
from apps.core.models import BaseModel
from apps.users.models import User
from apps.movies.models import Movie, Series

class Favourite(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.movie:
            return f"{self.user} ❤️ {self.movie}"
        return f"{self.user} ❤️ {self.series}"


class Review(BaseModel):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]  

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        target = self.movie if self.movie else self.series
        return f"{self.user} rated {target} - {self.rating}⭐"
