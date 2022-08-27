from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Password
from random import randint

@login_required
def get_password(request, password_length = 12):
    pw = generate_pw(request, password_length)
    return render(request, 'get_password.html', {"password": pw})

@login_required
def check_password(request, id):
    pw = Password(user = request.user, password="default")
    if Password.objects.filter(pk=id).exists():
        pw = Password.objects.get(pk=id)

    return render(request, 'get_password.html', {"password": pw})
    
def generate_pw(request, password_length):
    chars = ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)!@#$%&*()_+=-[]\{\};:\"'/?.>,<|\\"]
    chars_len = len(chars)
    new_password_str = ""
    for _ in range(password_length):
        new_password_str += chars[randint(0, chars_len)]
    pw = Password(user = request.user, password = new_password_str)
    pw.save()
    pw = Password.objects.get(pk=pw.pk)
    return pw