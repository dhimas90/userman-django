from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('userapp/index.html')
    return HttpResponse(template.render())

def register(request):
    template = "userapp/register.html"
    context = {}
    return render(request, template, context)