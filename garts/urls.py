"""garts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from home import views
from django.contrib.auth import views as auth_views
from quiz.views import QuizListView, QuizUserProgressView
from lesson.views import QuizView, register

quiz_urls = ([
    url(regex=r'^$',
        view=QuizListView.as_view(),
        name='quiz_index'),

    url(regex=r'^progress/$',
        view=QuizUserProgressView.as_view(),
        name='quiz_progress'),

    url(regex=r'^(?P<quiz_name>[\w-]+)/take/$',
        view=QuizView.as_view(),
        name='quiz_question'),
])

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^wordbrowser/', include('wordbrowser.urls')),
    url(r'', include('lesson.urls')),
    url(r'^quiz/', login_required(include(quiz_urls))),
    url(r'^login', auth_views.login, name='login'),
    url(r'^logout', auth_views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^register/', register),
    url(r'^accounts/', include('django.contrib.auth.urls'))
]
