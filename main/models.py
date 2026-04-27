from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название жанра")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название книги")
    author = models.CharField(max_length=255, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='books/', blank=True, null=True, verbose_name="Обложка")
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, verbose_name="Жанр")
    favorited_by = models.ManyToManyField(User, related_name='favorite_books', blank=True, verbose_name="В избранном у")

    def __str__(self):
        return self.title
    
class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название вечера")
    date = models.DateTimeField(verbose_name="Дата и время")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.title