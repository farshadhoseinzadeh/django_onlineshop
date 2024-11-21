from django.contrib import admin

from jalali_date.admin import ModelAdminJalaliMixin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ('order', 'product', 'quantity', 'price', )
    extra = 1


class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'datetime_created', 'is_paid',)
    ordering = ('-datetime_modified', '-datetime_created',)
    inlines = [
        OrderItemInline,
    ]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price', )
    ordering = ('-order', )


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
