from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from .views import completed_book, add_task, show_tasks, delete_task, edit_task


urlpatterns = [
    path('', completed_book, name='completed_book'),
    path('add_book/', add_task, name='add_book'),
    path('show_books/', show_tasks, name='show_books'),
    path('edit_book/<int:id>', edit_task, name='edit_book'),
    path('delete_book/<int:id>', delete_task, name='delete_task'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

