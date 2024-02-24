from django.urls import path
from .views import my_orders, track_order

app_name = 'orders'

urlpatterns = [
    path('my-orders/', my_orders, name='my_orders'),
    path('track-order/', track_order, name='track_order'),
    # Other URL patterns...
]