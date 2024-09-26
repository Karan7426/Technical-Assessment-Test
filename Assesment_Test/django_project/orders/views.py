from django.shortcuts import render
from .models import Order

def top_customers_view(request):
    top_customers = Order.get_top_customers()   
    context = {'top_customers': top_customers}
    return render(request, 'orders/top_customers.html', context)
