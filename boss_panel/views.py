from django.shortcuts import render, redirect
from .forms import TaskForm
from books.models import Books
# Create your views here.

# Home Page
def completed_book(request):
    # return redirect('completed_book')
    return render(request, 'boss_panel/boss_panel.html')


# Add Book 
def add_book(request):
    if request.method == 'POST':
        task = TaskForm(request.POST, request.FILES)
        # print(task.book_name)
        # print(task.description)
        # print(task.image)
        print(task)
        if task.is_valid():
            print("Task Form")
            task.save()
            # print(task.cleaned_data)
            return redirect('show_books')
    else:
        task = TaskForm()
    return render(request, 'boss_panel/add_book.html', {'task': task})


# Show Book List
def show_books(request):
    task = Books.objects.all()
    return render(request, 'boss_panel/show_books.html', {'task': task})


# Edit book
def edit_book(request, id):
    task = Books.objects.get(pk=id)
    form = TaskForm(instance = task)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_books')
    return render(request, 'boss_panel/edit_book.html', {'task': form})


# Delete Book
def delete_book(request, id):
    task = Books.objects.get(pk=id).delete()
    return redirect('show_books')

