from django import dispatch
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from datetime import date, datetime, timezone

from components.crud.models import Proyecto
from components.dashboard.forms import chartForm


# Create your views here.

class home(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       # context['latest_articles'] = Article.objects.all()[:5]

        return context


class charts(TemplateView):

    template_name = "charts.html"
    form_class = chartForm

    currentDateTime = datetime.now()
    date = currentDateTime.date()
    yearToday = date.strftime("%Y")
    yearInt = int(yearToday)
    proyectYearInCourse = Proyecto.objects.filter(year=yearInt)
    proyectPastYear = Proyecto.objects.filter(year=(yearInt-1))
    filtro = Proyecto.objects.all()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request.POST)
        if form.is_valid():
            pnf = form.cleaned_data['pnf']
            if pnf == "":
                filtro = self.filtro
                pnf = "Todas"
            else:
                filtro = Proyecto.objects.filter(pnf=pnf)
                context['proyectPnfAproved'] = filtro.filter(estado="Aprobado").count()
                context['proyectPnfNotAproved'] = filtro.filter(estado="Reprobado").count()
                context['proyectPnfInCourse'] = filtro.filter(estado="En curso").count()
                context["pnf"] = pnf
            
        return self.render_to_response(context)

            

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Gmayo: Bienvenido"
        context['title2'] = "Estadística"
        context['year'] = self.yearInt
        context['pastYear'] = self.yearInt-1
        context['form'] = chartForm
        context["pnf"] = "Todas"
 



      # Filtros carrera
        context['proyectPnfAproved'] = self.filtro.filter(estado="Aprobado").count()
        
        context['proyectPnfNotAproved'] = self.filtro.filter(estado="Reprobado").count()
        context['proyectPnfInCourse'] = self.filtro.filter(estado="En curso").count()


      # Filtros a#o en curso
        context['proyectYearInCourseAproved'] = self.proyectYearInCourse.filter(estado="Aprobado").count()
        
        context['proyectYearInCourseNotAproved'] = self.proyectYearInCourse.filter(estado="Reprobado").count()
        context['proyectYearInCourseInCourse'] = self.proyectYearInCourse.filter(estado="En curso").count()

      # Filtros a#o pasado
        context['proyectPastYearAproved'] = self.proyectPastYear.filter(estado="Aprobado").count()
        context['proyectPastYearNotAproved'] = self.proyectPastYear.filter(estado="Reprobado").count()
        context['proyectPastYearInCourse'] = self.proyectPastYear.filter(estado="En curso").count()

      # Filtros general
        context['proyectAproved'] = Proyecto.objects.filter(estado="Aprobado").count()
        
        context['proyectNotAproved'] = Proyecto.objects.filter(estado="Reprobado").count()
        context['proyectInCourse'] = Proyecto.objects.filter(estado="En Curso").count()

    

        return context

