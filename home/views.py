from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {}
    out = render(request, 'home/index.html', context)
    return out


def about(request):
    return render(request, 'home/about.html')