from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageViews(TemplateView):
    template_name = "index.html"

class AboutPageViews(TemplateView):
    template_name = 'about-us.html'













