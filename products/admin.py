from django.contrib import admin
from .models import Album, Genre, Track
from django_summernote.admin import SummernoteModelAdmin


class AlbumAdmin(SummernoteModelAdmin):
    list_display = (
        'genre',
        'name',
        'sku',
        'price',
        'rating',
    )
    summernote_fields = ('description')
    ordering = ('genre', 'name')


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


class TrackAdmin(admin.ModelAdmin):
    list_display = (
        'album',
        'name',
        'track_number',
    )


admin.site.register(Album, AlbumAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Track, TrackAdmin)
