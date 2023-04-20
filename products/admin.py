from django.contrib import admin
from .models import Album, Genre


class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        'genre',
        'name',
        'sku',
        'price',
        'rating',
    )

    ordering = ('genre', 'name')


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(Album, AlbumAdmin)
admin.site.register(Genre, GenreAdmin)
