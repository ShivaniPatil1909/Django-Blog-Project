from django.contrib import admin
from .models import Myblog, Profile, Comment

admin.site.register(Myblog)
admin.site.register(Profile)
admin.site.register(Comment)