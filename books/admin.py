from django.contrib import admin
from . models import Books

# Register your models here.
# admin.site.register(Product)

class BooksAdmin(admin.ModelAdmin):
    list_display = ['book_name', 'category', 'created_date', 'modified_date']
    prepopulated_fields = {'slug': ('book_name', )}
    
admin.site.register(Books, BooksAdmin)


