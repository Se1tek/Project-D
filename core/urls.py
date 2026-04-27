from django.contrib import admin
from django.urls import path
from main.views import (
    book_list, toggle_favorite, event_list, 
    profile_view, user_search, book_detail
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', book_list, name='book_list'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('favorite/<int:pk>/', toggle_favorite, name='toggle_favorite'),
    path('events/', event_list, name='event_list'),
    path('profile/', profile_view, name='profile'),
    path('search/', user_search, name='user_search'), # Исправлено: убрали views.
    path('favicon.ico', RedirectView.as_view(url='', permanent=True)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
