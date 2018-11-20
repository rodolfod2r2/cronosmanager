from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def dashboard(request):
    template = loader.get_template('dashboard.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def profile(request):
    template = loader.get_template('profile.html')
    context = {

    }
    return HttpResponse(template.render(context, request))