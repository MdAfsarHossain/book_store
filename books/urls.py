from django.urls import path
from .views import books, product_detail

urlpatterns = [
    path('', books, name = 'books'),
    
    path('category/<slug:category_slug>/', books, name = 'products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', product_detail, name = 'product_detail'),
    
]