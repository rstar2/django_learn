from django.shortcuts import render

# Create your views here.

# This is the Home page handler
def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)
