from django.shortcuts import render, get_object_or_404, redirect
from category.models import Category
from .models import Books, ReviewRating
from .forms import ReviewForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def books(request, category_slug=None):
    
    searchItem = request.GET.get('searchItem')
    if request.GET:
        if searchItem:
            books = Books.objects.filter(book_name__icontains=searchItem)
        else:
            books = Books.objects.all()
        context = {'searchItem': searchItem, 'books': books}
        return render(request, 'books/store.html', context)
        
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = Books.objects.filter(category=category)  # Category wise products
 
    else:
        # pass
        products = Books.objects.all()  # All products
    
    categories = Category.objects.all()
    context = {'books': products, 'categories': categories}

    return render(request, 'books/store.html', context)
    
    
    

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Books.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    
    reviews = ReviewRating.objects.filter(product_id=single_product.id)
    
    context = {
        'product': single_product,
        'reviews': reviews
    }
    return render(request, 'books/product_detail.html', context)
    
    


def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            review_rating = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=review_rating)
            if form.is_valid():
                form.save()
                messages.success(request, 'Thank you! Your review has been updated.')
            else:
                messages.error(request, 'Failed to update the review. Please check your input.')
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
            else:
                messages.error(request, 'Failed to submit the review. Please check your input.')


    product = get_object_or_404(Books, id=product_id)
    product_slug = product.slug
    category_slug = product.category.slug

    return redirect('product_detail', category_slug=category_slug, product_slug=product_slug)
        
    

def create_review(request, product_id):
    
    if request.method == 'POST':
        task = ReviewForm(request.POST)
        if task.is_valid():
            task.save()
            print(task.cleaned_data)
            return redirect('products_by_category')
    else:
        task = ReviewForm()
    return render(request, 'reviewform.html', {'task': task})

