# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Internal:
from .models import Album, Genre, Track
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class AlbumAdmin(SummernoteModelAdmin):
    """
    A class to register Album model in admin panel
    """
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
    """
    A class to register Genre model in admin panel
    """
    list_display = (
        'name',
        'friendly_name',
    )


class TrackAdmin(admin.ModelAdmin):
    """
    A class to register Track model in admin panel
    """
    list_display = (
        'album',
        'name',
        'track_number',
    )


admin.site.register(Album, AlbumAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Track, TrackAdmin)
