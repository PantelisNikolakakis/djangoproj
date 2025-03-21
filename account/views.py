from django.shortcuts import render, redirect

from .models import User

# Create your views here.

def login(request):
    return render(request, 'account/login.html')

def signup(request):
    if request.method == "POST":
        #print(request.POST)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if name and email and password1 and password2:
            user = User.objects.create_user(name, email, password1)

            print('user created')

            return redirect('/login/')
        else:
            print("sth went wrong")
    #else:
        #print('just show the form')
    return render(request, 'account/signup.html')