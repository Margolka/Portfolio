from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def home(request):
    t = loader.get_template("infos/home.html")
    return HttpResponse(t.render())


def me(request):
    t = loader.get_template("infos/me.html")
    return HttpResponse(t.render())


def contact(request):
    t = loader.get_template("infos/contact.html")
    return HttpResponse(t.render())
