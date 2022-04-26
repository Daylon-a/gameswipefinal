from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'splashpage.html')

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()

        messages.success(request, "Your account has been successfully created!")
        return redirect('signin')

    return render(request, 'signup.html')

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if User is not None:
            login(request, user)
            return render(request, 'splashpage.html', {'username':username})

        else:
            messages.error(request, "Incorrect Credentials!")
            return redirect('home')

    return render(request, 'signin.html')

def signout(request):

    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')

    