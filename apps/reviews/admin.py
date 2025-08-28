from django.contrib import admin
from .models import Review, Favourite

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "movie", "series", "rating", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("user__first_name", "user__last_name", "movie__name", "series__name")


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "movie", "series", "created_at")
    search_fields = ("user__first_name", "user__last_name", "movie__name", "series__name")
