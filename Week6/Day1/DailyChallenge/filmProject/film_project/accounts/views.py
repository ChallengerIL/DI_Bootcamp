from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


def signup(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('homepage')
    else:
        form = SignUpForm()

    context = {
        'title': 'Sign Up',
        'form': form
    }

    return render(request, 'registration/signup.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('homepage')
    else:
        form = LoginForm()

    context = {
        'title': 'Login',
        'form': form
    }

    return render(request, 'registration/login.html', context)


def logout_view(request):
    logout(request)


@login_required
def profile(request,):
    user = request.user

    context = {
        'title': f"{user.username}",
    }
    return render(request, 'accounts/profile.html', context)

