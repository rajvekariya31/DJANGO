from django.contrib import admin
from django.urls import path,include
from.views import *

urlpatterns = [
    path('',raj),
    path('post/',rajj),
    path('put/<id>/',raj2),
    path('patch/<id>/',raj3),
    path('delete/<id>/',raj4)
]

