from django.shortcuts import render
import random, string

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    all_characters = list(string.ascii_lowercase)
    if request.GET.get('uppercase'):
        all_characters.extend(list(string.ascii_uppercase))
    if request.GET.get('special'):
        all_characters.extend(list('!@#$%^&*()-_=+'))
    if request.GET.get('numbers'):
        all_characters.extend(list('0123456789'))

    thepass = ''
    lenght = int(request.GET.get('lenght', 8))
    for i in range(lenght):
        thepass += random.choice(all_characters)
    

    return render(request, 'generator/password.html', {'password': thepass})



