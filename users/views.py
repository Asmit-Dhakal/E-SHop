from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .froms import RegisterForm
from .models import User, Contact


# Create your views here
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome "{username}" your account created')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profilepage(request):
    user_objects = User.objects.all()
    return render(request, 'users/profile.html', {'user_objects': user_objects})


def handlelogout(request):
    logout(request)
    messages.info(request, "logout sucess")
    return redirect('login')
