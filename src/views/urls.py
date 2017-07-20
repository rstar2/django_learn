from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),  # name="home" -> name of the URL
    url(r'^about/$', views.about, name="about"),
    url(r'^contact/$', views.contact, name="contact"),
]
