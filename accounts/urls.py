from django.urls import path
from . import views

from .views import my_profile, edit_profile, change_password

app_name='accounts'

urlpatterns = [
    path('signup',views.signup,name='signup'),
    # path('<slug:slug>',views.profile,name='profile'),
    
    path('my-profile/', my_profile, name='my_profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('change-password/', change_password, name='change_password'),
    
    

    
]
