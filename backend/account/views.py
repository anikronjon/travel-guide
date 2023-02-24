from django.shortcuts import render
from .forms import UserSignUpForm
from django.http import HttpResponseRedirect

# User Registration View
def signup_view(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            password = form.cleaned_data['password']
            password.set_password()
            form.save()
            return HttpResponseRedirect('/account/signin/')

    else:
        form = UserSignUpForm()
    return render(request, 'account/signup.html', {'form': form})


def signin_view(request):
    return render(request, 'account/signin.html')