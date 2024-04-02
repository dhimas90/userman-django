from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    template = loader.get_template('userapp/index.html')
    return HttpResponse(template.render())


@login_required
def register(request):
    template = "registration/register.html"
    context = {}
    return render(request, template, context)