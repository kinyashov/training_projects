from django.contrib import admin
from .models import Performer, Album, Genre, Track


admin.site.register(Performer)
admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Track)
