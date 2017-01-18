from django.db import models
from django.utils.translation import ugettext as _
from true_false.models import TF_Question


class Word(models.Model):
    ARTICLES = (('der', 'der'), ('die', 'die'), ('das', 'das'))
    name = models.CharField(max_length=150)
    article = models.CharField(max_length=3, choices=ARTICLES)
    part_of_speech = models.CharField(max_length=50, blank=True)
    meaning = models.CharField(max_length=100, blank=True)
    extra = models.CharField(max_length=100, blank=True)
    figure = models.ImageField(upload_to='uploads/%Y/%m/%d',
                               blank=True,
                               null=True,
                               verbose_name=_("Figure"))
    rank_in_tops = models.IntegerField(null=True, default=-1)
    rank_in_dict = models.IntegerField(null=True, default=-1)
    source = models.CharField(max_length=150, default='Not set')

    def save(self, *args, **kwargs):
        is_new = not self.id
        super(Word, self).save(*args, *kwargs)
        if is_new:
            art_question = ArticleQuestion(related_word_id=self, content=self.name, article=self.article, figure=self.figure)
            art_question.save()

    def __str__(self):
        return self.name


class ArticleQuestion(TF_Question):

    article = models.CharField(blank=False,
                               default=False,
                               max_length=3)

    related_word_id = models.ForeignKey(Word, verbose_name=_("Question"))

    def check_if_correct(self, guess):
        if guess == self.article:
            return True
        else:
            return False

    def get_answers(self):

        return[{'correct': self.check_if_correct("der"),
                'content': 'der'},
               {'correct': self.check_if_correct("die"),
                'content': 'die'},
               {'correct': self.check_if_correct("das"),
                'content': 'das'
                }]

    def get_answers_list(self):
        return Word.ARTICLES

    def answer_choice_to_string(self, guess):
        return str(guess)
