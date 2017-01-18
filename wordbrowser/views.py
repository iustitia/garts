from django.shortcuts import render, get_object_or_404

from lesson.models import Word


def index(request):
    words = Word.objects.order_by('id')

    context = {'wordlist': words}

    out = render(request, 'wordbrowser/index.html', context)
    return out


def detail(request, word_id):
    word = get_object_or_404(Word, pk = word_id)

    context = {'word': word}

    out = render(request, 'wordbrowser/detail.html', context)

    return out


# deprecated lesson - keep for reference for initial UI
def lesson(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    context = {'word': word}

    out = render(request, 'wordbrowser/lesson.html', context)

    return out
