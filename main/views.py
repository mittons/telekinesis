from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'test.html')

def home2(request):
    return HttpResponse("Halló Sól og Máni!")
