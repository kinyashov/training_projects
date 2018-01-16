from django.contrib import admin
from .models import User, Twit, Like, Reply


admin.site.register(User)
admin.site.register(Twit)
admin.site.register(Like)
admin.site.register(Reply)
