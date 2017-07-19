"""crumpa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from views import views
# from profiles import views as profiles_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Needed for Django-allauth
    url(r'^' + settings.ACCOUNT_URL_PREFIX + r'/', include('allauth.urls')),

    url(r'^$', views.home, name="home"),  # name="home" -> name of the URL
    url(r'^about/$', views.about, name="about"),
    url(r'^contact/$', views.contact, name="contact"),

    # include all ulrs in the 'profiles' app under a single path
    url(r'^profiles/', include('profiles.urls')),
]

# By default, the development server doesn’t serve any static files for your site
# (such as CSS files, images, things under MEDIA_URL and so forth).
# It has to be configured explicitely if wanted "$ python manage.py runserver" to server them
# !!! THIS SHOULD BE DONE ONLY IN DEVELOPMENT MODE, NOT PRODUCTION
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)