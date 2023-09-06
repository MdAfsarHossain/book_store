from django.shortcuts import render, redirect
from .forms import TaskForm
from books.models import Books
# Create your views here.

# Home Page
def completed_book(request):
    # return redirect('completed_book')
    return render(request, 'boss_panel/boss_panel.html')


# Add Todo List
def add_task(request):
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
            # print(task.cleaned_data)
            return redirect('show_books')
    else:
        task = TaskForm()
    return render(request, 'boss_panel/add_book.html', {'task': task})


# Show Todo List
def show_tasks(request):
    task = Books.objects.all()
    return render(request, 'boss_panel/show_books.html', {'task': task})


# Edit Todo List
def edit_task(request, id):
    task = Books.objects.get(pk=id)
    form = TaskForm(instance = task)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_books')
    return render(request, 'boss_panel/edit_book.html', {'task': form})


# Delete Todo List
def delete_task(request, id):
    task = Books.objects.get(pk=id).delete()
    return redirect('show_books')


# Complete Todo List
# def completed_tasks(request, id=None):
#     if id is None:
#         tasks = Books.objects.all()
#         return render(request, 'completed_tasks.html', {'task': tasks})
#     else:
#         tasks = Books.objects.get(pk=id)
#         tasks.is_completed = True
#         tasks.save()
#         return redirect('completed_tasks_default')
      
      
      
