from django.contrib import admin

from .models import Customer

# Register your models here.
# class UserAccountAdmin(admin.ModelAdmin):
    # list_display = ('username', 'first_name', 'last_name', 'email')

# admin.site.register(Customer, UserAccountAdmin)

admin.site.register(Customer)
