from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'active', 'datetime_created', 'datetime_modified')
    ordering = ('-datetime_modified', '-datetime_created',)


admin.site.register(Product, ProductAdmin)
