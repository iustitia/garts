from django.contrib import admin
from .models import ArticleQuestion, Word


class ArticleQuestionAdmin(admin.ModelAdmin):
    list_display = ('content', 'category', )
    list_filter = ('category', 'related_word_id')
    fields = ('content', 'category', 'sub_category',
              'figure', 'quiz', 'explanation',)

    search_fields = ('content', 'explanation')
    filter_horizontal = ('quiz',)


class WordAdmin(admin.ModelAdmin):
    fields = ('name', 'article', 'meaning', 'part_of_speech',
              'figure', 'extra',)


# Register your models here.
admin.site.register(ArticleQuestion, ArticleQuestionAdmin)
admin.site.register(Word, WordAdmin)
