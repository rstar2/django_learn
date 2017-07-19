from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.all, name="profiles_all"),
    url(r'^(?P<profile_id>.+)/$', views.get, name="profiles_get"),
]
