from django.shortcuts import render

# Create your views here.
# orders/views.py
from django.shortcuts import render

def my_orders(request):
    # Your view logic here
    return render(request, 'my-orders.html')

def track_order(request):
    # Your view logic here
    return render(request, 'track-order.html')
