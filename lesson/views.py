from django.shortcuts import render, get_object_or_404, redirect
from .models import Word
from quiz.models import Quiz, Category
import uuid
from random import randint


def index(request):
    context = {}
    out = render(request, 'lesson/index.html', context)

    return out


def lesson(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    context = {'word': word}

    out = render(request, 'lesson/lesson.html', context)


def make_quiz(request, random=True, count=10):
    name = uuid.uuid4().hex[:10]
    q = Quiz(title=name, url=name, category=Category.objects.first(), random_order=True, answers_at_end=True, exam_paper=True)
    q.save()
    questions = [randint(1,170) for _ in range(count)]
    q.question_set = questions
    out = redirect('/quiz/' + name + '/take/')

    return out
