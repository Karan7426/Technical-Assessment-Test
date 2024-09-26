from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order_date', 'status', 'total_amount')
    search_fields = ('customer__username',)
    list_filter = ('status',)

