from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """Модель Поста"""
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

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        """Возвращает заголовок поста, если объект представляется в виде строки"""
        return self.title


class Comment(models.Model):
    """Модель Комментария"""
    post = models.ForeignKey(
        'blog.Post',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
