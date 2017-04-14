import sys
from django.core.management.base import BaseCommand
from lesson.models import Word
import argparse


class Command(BaseCommand):
    help = "Add batch words from specified file."

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='?', type=argparse.FileType('r'), default=sys.stdin)

    def handle(self, *args, **options):
        print(options)
        sourcefile = options['path']

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
