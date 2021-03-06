from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from expense_tracker.forms import RegistrationForm, AuthenticationForm, UpdateForm


# Create your views here.
def registration_view(request):
    context= {}
    if request.POST:
        forms= RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email= form.cleaned_data.get('email')
            password= form.cleaned_data.get('password1')
            account= authenticate(email= email, password= password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form']= form

    else:
        form= RegistrationForm()
        context['registration_form']= form
    return render(request, 'expense_tracker/register.html', context)

def logout(request):
    logout(request)
    return redirect('home')

def login(request):
    context= {}
    user= request.user
    if user.is_authenticated:
        return redirect("home")
    if request.POST:
        form= AuthenticationForm(request.POST)
        if form.is_valid():
            email= request.POST['email']
            password= request.POST['password']
            user = authenticate(email= email, password= password)
            if user:
                login(request, user)
                return redirect("home")

    else:
        form= AuthenticationForm()
    
    context['login_form']= form
    return render(request, 'expense_tracker/login.html', context)

def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    context= {}
    if request.POST:
        form= UpdateForm(request.POST, instance= request.user)
        if form.is_valid():
            form.save()
        else:
            form= UpdateForm(
                initial= {
                    "email": request.user.email,
                    "username": request.user.username
                }
            )
    
    context['account_form']= form
    return render(request, 'expense_tracker/update.html', context)


    



