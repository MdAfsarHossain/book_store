from django.shortcuts import render, get_object_or_404
from books.models import Books
from category.models import Category
# Create your views here.

def home(request, category_slug=None):
    
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = Books.objects.filter(category=category)  # Category wise products
        
    else:
        products = Books.objects.all()  # All products
    
    categories = Category.objects.all()
    context = {'products': products, 'categories': categories, }
    # context = {'categories': categories, }
    return render(request, 'index.html', context)
    # return render(request, 'index.html')
    