from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from accounts.forms import UserLoginForm, UserRegistrationForm
from accounts.models import User
from util.encoder import encode_md5


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            password = data['password']
            encoded_password = encode_md5(password)
            email = data['email']

            user = authenticate(request, email=email, password=encoded_password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Успішна авторизація', 'success')
                return redirect('shop:home')
            else:
                messages.error(request, 'Логін чи пароль неправильний!', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'Успішна авторизація', 'success')
    return redirect('shop:home')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(data['email'], data['full_name'], data['phone_number'], data['password'])
            login(request, user)
            messages.success(request, 'Регістрація успішна!', 'success')
            return redirect('shop:home')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
