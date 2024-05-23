from django.http import HttpResponse
from django.shortcuts import render

def Test(request):
    data={'name':'rakib','salary':'10000'}
    return render(request,'index.html',data)