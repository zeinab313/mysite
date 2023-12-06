from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse('<h1>index home</h1>')

def about_view(request):
    return HttpResponse('<h1>about </h1>')

def contact_view(request):
    return HttpResponse('<h1>contact </h1>')