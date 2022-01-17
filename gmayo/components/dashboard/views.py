from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class home(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       # context['latest_articles'] = Article.objects.all()[:5]
        return context


class contact(TemplateView):

    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       # context['latest_articles'] = Article.objects.all()[:5]
        return context