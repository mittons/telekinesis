from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')

def technology(request):
    return render(request, 'technology.html')

def travel(request):
    return render(request, 'travel.html')

def food(request):
    return render(request, 'food.html')

def fashion(request):
    return render(request, 'fashion.html')

def blogposttemplate(request):
    return render(request, 'blogposttemplate.html')

def blogwysiwygtest(request):
    return render(request, 'blogwysiwygtest.html')

