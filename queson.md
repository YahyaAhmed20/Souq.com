
this views.py belong to accounts apps i want to make this code with slug def my_profile(request):
    # Your view logic here
    return render(request, 'profile.html')

def edit_profile(request):
    # Your view logic here
    return render(request, 'edit_profile.html')

def change_password(request):
    # Your view logic here
    return render(request, 'change-password.html')




    this views.py belong to orders apps i want to make this code with slug 


    from django.shortcuts import render

def my_orders(request):
    # Your view logic here
    return render(request, 'my-orders.html')

def track_order(request):
    # Your view logic here
    return render(request, 'track-order.html')
 