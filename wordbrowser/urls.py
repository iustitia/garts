from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(views.index), name='index'),
    url(r'^(?P<word_id>[0-9]+)/$', login_required(views.detail), name='detail'),
]