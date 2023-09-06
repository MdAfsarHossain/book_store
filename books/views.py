from django.shortcuts import render, get_object_or_404, redirect
from category.models import Category
from .models import Books
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

def books(request, category_slug=None):
    
    searchItem = request.GET.get('searchItem')
    if request.GET:
        if searchItem:
            foods = Books.objects.filter(book_name__icontains=searchItem)
        else:
            foods = Books.objects.all()
        context = {'searchItem': searchItem, 'foods': foods}
        return render(request, 'books/store.html', context)
        
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = Books.objects.filter(category=category)  # Category wise products
 
    else:
        # pass
        products = Books.objects.all()  # All products
    
    categories = Category.objects.all()
    context = {'foods': products, 'categories': categories}

    return render(request, 'books/store.html', context)
    

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Books.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    
    context = {
        'product': single_product,
    }
    return render(request, 'store/product_detail.html', context)
    
    
