from django.http import HttpResponse
from django.shortcuts import render

def Test(request):
    data={'name':'mD Rakib Bhuiyan','salary':'10000'}
    return render(request,'index.html',data)