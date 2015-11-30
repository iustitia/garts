from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index2(request):

    return HttpResponse("Hello world, main page works.")


def index(request):

    context = {}

    out = render(request, 'home/index.html', context)
    return out
