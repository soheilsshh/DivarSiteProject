from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request , data = request.POST)
        if form.is_valid():
            login(request , form.get_user())
            return redirect('home')
    
    else:
        form = AuthenticationForm()
    return render(request , "login.html" , {'form' : form})