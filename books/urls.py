from django.urls import path
from .views import books, product_detail, submit_review


from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', books, name = 'books'),
    
    path('category/<slug:category_slug>/', books, name = 'products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', product_detail, name = 'product_detail'),
    
        
    path('submit_review/<int:product_id>/', submit_review, name='submit_review'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)