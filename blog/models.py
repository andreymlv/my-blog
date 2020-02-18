from django.conf import settings
from django.db import models
from django.utils import timezone

# Модель поста


class Post(models.Model):
    # Автор
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    # Заголовок
    title = models.CharField(max_length=200)
    # Текст
    text = models.TextField()
    # Дата создания
    created_date = models.DateTimeField(default=timezone.now)
    # Дата публикации
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """Метод публикации поста"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """Возвращает заголовок поста, если объект представляется в виде строки"""
        return self.title
