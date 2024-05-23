from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myApp(request):
    return render(request,'MyApp/index1.html')


def Hello(request):
    return render(request,'MyApp/index.html')
