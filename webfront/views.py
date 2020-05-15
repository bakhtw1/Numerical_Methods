# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def styles(request):
    return render(request, 'styles.css', {}, content_type='text/css')