from django.contrib import admin
from .models import Actor, Movie, Series

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "specialization")
    search_fields = ("name", "specialization")


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "duration", "watch_count", "is_franchise")
    list_filter = ("is_franchise", "category")
    search_fields = ("name",)


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    search_fields = ("name",)

