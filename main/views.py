from django.shortcuts import render
from .models import Book # Импортируем модель
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book # Импортируем твою модель
from django.contrib.auth.models import User  # Обязательно для работы поиска и профиля
from django.db.models import Q               # Нужно для сложного поиска
from .models import Event
from django.contrib.auth.models import User # Исправляет NameError со скриншота 8

# def book_list(request):
#     return render(request, 'books/book_list.html')

def event_list(request):
    events = Event.objects.all() # Без этой строки список будет пустым
    return render(request, 'books/event_list.html', {'events': events})

def profile_view(request):
    # Берем книги, которые пользователь добавил в избранное
    favorite_books = request.user.favorite_books.all()
    
    # Берем других пользователей (как друзей)
    friends = User.objects.exclude(id=request.user.id)[:5] 

    return render(request, 'books/profile.html', {
        'favorite_books': favorite_books,
        'friends': friends,
        'reading_history': favorite_books.order_by('-id') # История на основе избранного
    })

def user_search(request):
    query = request.GET.get('q')
    users = User.objects.none() # По умолчанию пустой список
    
    if query:
        # Ищем по нику или по ID
        users = User.objects.filter(
            Q(username__icontains=query) | Q(id__iexact=query)
        )
    
    return render(request, 'books/user_search.html', {'users': users, 'query': query})

def book_detail(request, pk):
    # Эта строка берет ID из URL и ищет книгу в базе данных
    book = get_object_or_404(Book, pk=pk) 
    # Передаем переменную 'book' в ваш HTML-шаблон
    return render(request, 'books/book_detail.html', {'book': book})

def toggle_favorite(request, pk):
    # Пока просто возвращаем пользователя обратно на список книг
    return redirect('book_list')

def book_list(request):
    books = Book.objects.all() # Хватаем все книги из базы
    return render(request, 'books/book_list.html', {'books': books})

# Тот самый toggle_favorite, на который ругался Django
def toggle_favorite(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.user in book.favorited_by.all():
        book.favorited_by.remove(request.user)
    else:
        book.favorited_by.add(request.user)
    return redirect('book_list')