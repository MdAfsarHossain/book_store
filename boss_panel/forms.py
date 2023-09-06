from django import forms
from books.models import Books

class TaskForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['book_name', 'description', 'image', 'category']
