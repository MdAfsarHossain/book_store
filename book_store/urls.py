from django.contrib import admin
from django.urls import path, include
from .views import home
from books.views import product_detail

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('accounts.urls')),
    
    path('book/', include('books.urls')),
    path('boss/', include('boss_panel.urls')),
    
    path('category/<slug:category_slug>/<slug:product_slug>/', product_detail, name = 'product_detail'),
    
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
