from django.shortcuts import render, HttpResponseRedirect, reverse
from custom_user.models import CustomUser
from custom_user.forms import LoginForm, SignupForm
from custom_proj.settings import AUTH_USER_MODEL
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def index(request):
    return render(request, 'index.html', {'user_string': AUTH_USER_MODEL})


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = CustomUser.objects.create_user(
                username=data.get('username'), password=data.get('password'), display_name=data.get('display_name'))
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))

    form = SignupForm()
    return render(request, 'generic_form.html', {'form': form, 'user_string': AUTH_USER_MODEL})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username=data.get("username"), password=data.get("password"))
        if user:
            login(request, user)
            return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))

    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form, 'user_string': AUTH_USER_MODEL})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
