from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import UserSignInForm, UserSignUpForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


# User SignIn View
def signin_view(request):
    if request.method == 'POST':
        form = UserSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user=user)
            return HttpResponseRedirect('/profile/')
    else:
        form = UserSignInForm()
    return render(request, 'accounts/signin.html', {'form': form})


# User SignUp View
def signup_view(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/signin/')

    else:
        form = UserSignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


# User Dashboard
@login_required
def profile_view(request):
    return render(request, 'accounts/dashboard.html', {'user': request.user})
