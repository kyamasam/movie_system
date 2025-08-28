from django.db import models
from apps.core.models import BaseModel, Category, ScreenRole
from apps.users.models import User

class Actor(BaseModel):
    name = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to="actors/")
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    video_link = models.URLField()
    intro_length = models.FloatField()
    outro_length = models.FloatField()
    duration = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cover_photo = models.ImageField(upload_to="movies/")
    watch_count = models.PositiveIntegerField(default=0)
    is_franchise = models.BooleanField(default=False)
    prequel = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="prequel_movie")
    sequel = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="sequel_movie")

    def __str__(self):
        return self.name


class Series(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cover_photo = models.ImageField(upload_to="series/")

    def __str__(self):
        return self.name
