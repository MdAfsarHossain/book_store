from django.contrib import admin
from django.urls import path, include
from .views import home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('accounts.urls')),
    
    path('book/', include('books.urls')),
    path('boss/', include('boss_panel.urls')),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
