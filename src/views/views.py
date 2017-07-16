from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

from .forms import ContactForm

# Create your views here.

def home(request):
    """ This is the Home page handler """
    context = locals()
    template = 'home.html'
    return render(request, template, context)


def about(request):
    context = locals()
    template = 'about.html'
    return render(request, template, context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        email_from = form.cleaned_data["email"]
        name = form.cleaned_data["name"]
        comment = form.cleaned_data["comment"]
        message = '%s %s' % (name, comment)

        send_mail(
            'Contact me :',
            message,
            email_from,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        # return redirect("home")
        return HttpResponse("OK")

    context = {'form': form}
    template = 'contact.html'
    return render(request, template, context)


@login_required
def profile(request):
    context = locals()
    template = 'profile.html'
    return render(request, template, context)
