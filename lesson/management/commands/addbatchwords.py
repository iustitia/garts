import os
from django.core.management.base import BaseCommand
from lesson.models import Word


class Command(BaseCommand):
    help = "Add batch words from specified file."

    def handle(self, *args, **options):
        sourcefile = '/home/germanarticles/data/top_articled.txt'

        with open(sourcefile, 'r') as f:
            content = f.readlines()

            for nr, line in enumerate(content):

                l = str.split(line, '] [')

                a = str.strip(l[0], '[\'').split()
                w = a[0].strip(',').replace('\\xad', '')
                article = a[1].strip(',')

                rank = line.count('▮')

                new_word = Word(name=w, article=article, rank_in_tops=nr, source='tatoeba', rank_in_dict=rank)
                new_word.save()
