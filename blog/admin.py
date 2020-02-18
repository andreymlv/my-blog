from django.contrib import admin
from .models import Post
# Регестрируем модель в админке
admin.site.register(Post)
