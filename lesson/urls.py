from django.conf.urls import url
from . import views

urlpatterns = [
    url( r'^$', views.index, name='index'),
    url(r'^(?P<word_id>[0-9]+)/^$', views.lesson, name='lesson')
]
