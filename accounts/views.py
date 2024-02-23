from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Profile
from django.contrib.auth import login, authenticate
from .forms import UserForm, ProfileForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']  # Use 'password1' for the first password field
            
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/products')
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'registration/signup.html', context)


def profile(request,slug):
    profile=get_object_or_404(Profile, slug=slug)
    context= {"profile":profile}
    return render (request,"profile.html",context)
