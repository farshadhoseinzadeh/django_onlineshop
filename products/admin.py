from django.contrib import admin

from .models import Product, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ('author', 'body', 'stars', 'active', )
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'active', 'datetime_created', 'datetime_modified',)
    ordering = ('-datetime_modified', '-datetime_created',)
    inlines = [
        CommentInline,
    ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'author', 'body', 'stars', 'active', 'datetime_created', 'datetime_modified',)
    ordering = ('-datetime_modified', '-datetime_created',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
