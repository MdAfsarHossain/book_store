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
    

    

RATING = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
) 

    
class ReviewRating(models.Model):
    product = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(max_length=500, blank=True)
    rating = models.IntegerField(choices=RATING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review

