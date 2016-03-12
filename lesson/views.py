from django.shortcuts import render, get_object_or_404
from .models import Word


def index(request):
    context = {}
    out = render(request, 'lesson/index.html', context)

    return out


def lesson(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    context = {'word': word}

    out = render(request, 'lesson/lesson.html', context)