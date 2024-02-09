from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from django.core.paginator import Paginator ,EmptyPage, PageNotAnInteger

# Create your views here.   

def product_list(request):
    product_list=Product.objects.all()
    # paganator
    paginator = Paginator(product_list, 2)  # Show 25 contacts per page.
    page= request.GET.get("page")
    product_list = paginator.get_page(page)
    

    context={'product_list':product_list}
    return render(request,'Product/product_list.html',context)

def product_details(request,id):
    product_details=Product.objects.get(id=id)
    context={'product_details':product_details}
    return render(request,'Product/product_details.html',context)