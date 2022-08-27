from netrc import netrc
from urllib.request import HTTPRedirectHandler
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import ScrambledPassword
from random import randint, sample

@login_required
def get_password(request, password_length = 8, number_chars = 2, special_chars = 2):
    if not type(password_length) == int or not type(number_chars) == int or not type(special_chars) == int:
        return HttpResponseRedirect("/password/get")
    if password_length < 4 or number_chars < 0 or special_chars < 0:
        return HttpResponseRedirect("/password/get")
    if password_length < number_chars + special_chars:
        return HttpResponseRedirect("/password/get")

    pw = generate_new_pw(request, password_length, number_chars, special_chars)
    return render(request, 'get_password.html', {"password": pw})

@login_required
def check_password(request, id):
    pw = ScrambledPassword(user = request.user, text="default")
    if ScrambledPassword.objects.filter(pk=id).exists():
        pw = ScrambledPassword.objects.get(pk=id)
    else:
        return HttpResponseRedirect("/password/get")

    return render(request, 'check_password.html', {"password": pw})
    
def generate_new_pw(request, password_length = 8, numbers = 2, specials = 2):
    alpha_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY"
    number_chars = "0123456789"
    special_chars = "!@#$%&*()_+=?"
    new_password_str = ""
    for _ in range(password_length - specials - numbers):
        x = randint(0, len(alpha_chars)-1)
        new_password_str += alpha_chars[x]
    for _ in range(numbers):
        x = randint(0, len(number_chars)-1)
        new_password_str += number_chars[x]
    for _ in range(specials):
        x = randint(0, len(special_chars)-1)
        new_password_str += special_chars[x]
    new_password_str = ''.join(sample(new_password_str,len(new_password_str)))
    pw = ScrambledPassword(user = request.user, text = new_password_str)
    pw.save()
    pw = ScrambledPassword.objects.get(pk=pw.pk)
    return pw