from django.shortcuts import render
from django.http import HttpResponse
import random
import string


# Create your views here.

def dafault_page(request):
    return HttpResponse("This is the default Home page.<br><h1>Welcome!</h1>")

def home(request):
    return render(request, 'string_generator/home.html',{'dict_key':'value'})

def password_generator_page(request):
    return render(request, 'string_generator/password_generator_page.html')

def generated_password_page(request):

    generated_password = ''

    #lst = list("abcdefghijklmnopqrstuvwxyz")
    characters = string.ascii_letters
    string_of_characters = characters[0:26]

    if request.GET.get('small_capital'):
        string_of_characters = characters

    if request.GET.get('number'):
        string_of_characters += "0123456789"

    if request.GET.get('special_char'):
        string_of_characters += "!@#$&*_-!@#$&*_-"

    password_length = int(request.GET.get('length'))

    for temp in range(password_length):
        generated_password += random.choice(string_of_characters)

    #lst.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return render(request, 'string_generator/generated_password_page.html', {'generated_password':generated_password})

#, {'generated_password_value':password_length}


def about_page(request):
    return render(request, 'string_generator/about_page.html')
