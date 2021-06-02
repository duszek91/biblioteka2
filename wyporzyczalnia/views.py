from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UserRegisterForm
from .models import Book


def contact(request):
    return render(request, 'contact.html', {})


def index(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def all_books(request):
    books = Book.objects.all()
    return render(request, 'listofbooks.html', {'books': books})