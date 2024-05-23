from django.urls import path
from . import views

urlpatterns=[
    path('a/',views.myApp),
    path('',views.Hello)
]