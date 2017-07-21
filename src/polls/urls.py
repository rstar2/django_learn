from django.conf.urls import url

from . import views

# this will give a namespace for ALL the views
# so they will have to be used like:
#  {% url 'polls:index' %}
#  {% url 'polls:detail' 1 %}
app_name = 'polls'


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]