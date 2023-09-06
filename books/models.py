from django.db import models
from django.contrib.auth.models import User
from category.models import Category
from django.urls import reverse

# Create your models here.

class Books(models.Model):
    book_name = models.CharField(max_length = 100, unique=True)
    slug = models.SlugField(max_length=200, unique = True)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='photos/book')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    
    def __str__(self):
        return self.book_name
    


