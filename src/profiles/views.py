from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def all(request):
    context = locals()
    template = 'profile.html'
    return render(request, template, context)


@login_required
def get(request, profile_id):
    context = {'id': profile_id}
    template = 'profile.html'
    return render(request, template, context)
