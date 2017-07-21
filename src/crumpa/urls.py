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

urlpatterns = [
    # Django admin module
    url(r'^admin/', admin.site.urls),

    # Django-allauth 
    url(r'^' + settings.ACCOUNT_URL_PREFIX + r'/', include('allauth.urls')),

    # include all main urls in the 'views' app under the main root
    url(r'^', include('views.urls')),

    # include all urls in the 'profiles' app under a single root - "/profiles"
    url(r'^profiles/', include('profiles.urls')),

    # added the 'polls' app from the Dajbago Tutorial
    url(r'^polls/', include('polls.urls')),
]

# By default, the development server doesn’t serve any static files for your site
# (such as CSS files, images, things under MEDIA_URL and so forth).
# It has to be configured explicitely if wanted "$ python manage.py runserver" to server them
# !!! THIS SHOULD BE DONE ONLY IN DEVELOPMENT MODE, NOT PRODUCTION
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)