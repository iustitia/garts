from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import Word
from quiz.models import Quiz, Category, Progress
from quiz.views import QuizTake
import uuid
from random import randint
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required


def index(request):
    context = {}
    out = render(request, 'lesson/index.html', context)

    return out


def lesson(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    context = {'word': word}

    out = render(request, 'lesson/lesson.html', context)

@login_required
def make_quiz(request, random=True, count=10):
    name = uuid.uuid4().hex[:10]
    q = Quiz(title=name, url=name, category=Category.objects.first(), random_order=True, answers_at_end=True, exam_paper=True, single_attempt=True)
    q.save()
    count = int(count)
    questions = [randint(1,170) for _ in range(count)]
    q.question_set = questions
    out = redirect('/quiz/' + name + '/take/')

    return out


class QuizView(QuizTake):
    @login_required
    def form_valid_user(self, form):
        progress, c = Progress.objects.get_or_create(user=self.request.user)
        guess = form.cleaned_data['answers']
        is_correct = self.question.check_if_correct(guess)

        if is_correct is True:
            self.sitting.add_to_score(1)
            progress.update_score(self.question, 1, 1)
        else:
            self.sitting.add_incorrect_question(self.question)
            progress.update_score(self.question, 0, 1)

        self.previous = {}
        #TODO fix problem with previous question result

        self.sitting.add_user_answer(self.question, guess)
        self.sitting.remove_first_question()

    def final_result_user(self):
        out = super(QuizView, self).final_result_user()

        if self.quiz.single_attempt:
            self.quiz.delete()

        return out


def register(request):
    if request.method == 'POST':
        uf = RegistrationForm(request.POST, prefix='user')
        if uf.is_valid():
            user = uf.save()
            return redirect('/login')
    else:
        uf = RegistrationForm(prefix='user')
    return render(request, 'register.html', {'form': uf})
