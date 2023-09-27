from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from .views import completed_book, add_book, show_books, delete_book, edit_book


urlpatterns = [
    path('', completed_book, name='completed_book'),
    path('add_book/', add_book, name='add_book'),
    path('show_books/', show_books, name='show_books'),
    path('edit_book/<int:id>', edit_book, name='edit_book'),
    path('delete_book/<int:id>', delete_book, name='delete_task'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

