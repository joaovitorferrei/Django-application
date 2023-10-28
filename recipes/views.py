from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# return HTTP response
def home(request):
    return render(request, 'recipes/home.html')

def contato(request):
    return HttpResponse('ola tudo bem')

def sobre(request):
    return HttpResponse('esse é meu sobre')
    