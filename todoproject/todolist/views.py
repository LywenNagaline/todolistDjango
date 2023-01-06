from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView

def index(request):
    return HttpResponse("Bienvenue sur l'application !")

class AboutView(TemplateView):
    template_name = "about.html"