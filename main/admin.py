from django.contrib import admin
from .models import Book, Genre
from .models import Genre, Book, Event # Добавь Event в импорт

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Event) # Регистрируем мероприятия