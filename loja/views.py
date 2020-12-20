from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context = {
        'title':'HOME PAGE',
        'content':'Bem vindo a nossa Home Page:)'
        }
    return render(request, 'homepage.html', context)

    