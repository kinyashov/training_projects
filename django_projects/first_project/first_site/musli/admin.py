from django.contrib import admin
from .models import Performer, Album, Genre, Track


class PerformerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('genre',)}


admin.site.register(Performer, PerformerAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Track)
