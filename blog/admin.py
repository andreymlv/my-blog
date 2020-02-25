from django.contrib import admin
from .models import Post, Comment
# Регестрируем модель в админке
admin.site.register(Post)
admin.site.register(Comment)
