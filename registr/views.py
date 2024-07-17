from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def SignPage(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                name = 'username exists!'
                return render(request, 'registr/sign.html', {'name': name})
            if User.objects.filter(email=email).exists():
                pochta = 'email address exists!'
                return render(request, 'registr/sign.html', {'pochta': pochta})
            else:
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                user.save()
                login(request, user)
                return redirect('home')
        else:
            hato = 'passwords didn\'t match!'
            return render(request, 'registr/sign.html', {'hato': hato})
    return render(request, 'registr/sign.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            hato = 'username or password error!'
            return render(request, 'registr/login.html', {'hato': hato})
    return render(request, 'registr/login.html')


def LogoutPage(request):
    logout(request)
    return redirect('home')