from django.shortcuts import render
from django.views.generic.base import TemplateView
from datetime import date, datetime, timezone

from components.crud.models import Proyecto


# Create your views here.

class home(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       # context['latest_articles'] = Article.objects.all()[:5]
        return context


class charts(TemplateView):

    template_name = "index.html"

    currentDateTime = datetime.now()
    date = currentDateTime.date()
    yearToday = date.strftime("%Y")
    yearInt = int(yearToday)
    proyectYearInCourse = Proyecto.objects.filter(year=yearInt)
    proyectPastYear = Proyecto.objects.filter(year=(yearInt-1))


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            year = form.cleaned_data['years']
            responsable = form.cleaned_data['responsable']
            estado = form.cleaned_data['estado']
            pnf = form.cleaned_data["pnf"]


            if estado == "" and responsable == None and year =="0" and pnf == "" :
                filtro = Proyecto.objects.all()
                print(1)
                
                
            elif estado != "" and responsable !=None and year !="0" and pnf != "" :
                filtro = Proyecto.objects.filter(responsable=responsable).filter(pnf=pnf).filter(year=year).filter(estado=estado)
                print(12)
            

            elif estado == "" and year =="0" and pnf =="" :
                filtro = Proyecto.objects.filter(responsable=responsable)
                print(13)
            
            elif responsable == None and year =="0" and pnf =="" :
                filtro = Proyecto.objects.filter(estado=estado)
                print(14)
            
            elif estado == "" and responsable ==None and pnf =="" :
                filtro = Proyecto.objects.filter(year=year)
                print(15)
          
            elif estado == "" and year =="0" and responsable ==None :
                filtro = Proyecto.objects.filter(pnf=pnf)
                print(16)
          



            elif estado == "" and year =="0" :
                filtro = Proyecto.objects.filter(responsable=responsable).filter(pnf=pnf)
                print(17)
          
            elif responsable == None and year =="0" :
                filtro = Proyecto.objects.filter(estado=estado).filter(pnf=pnf)
                print(18)
          
            elif pnf == "" and year =="0" :
                filtro = Proyecto.objects.filter(responsable=responsable).filter(estado=estado)
                print(19)
          
            elif estado == "" and responsable ==None :
                filtro = Proyecto.objects.filter(year=year).filter(pnf=pnf)
                print(100)
          
            elif estado == "" and pnf =="" :
                filtro = Proyecto.objects.filter(responsable=responsable).filter(year=year)
                print(101)
          
            elif responsable == None and pnf =="" :
                filtro = Proyecto.objects.filter(year=year).filter(estado=estado)
                print(102)
          

            
            
            elif year == "0" :
                filtro = Proyecto.objects.filter(responsable=responsable).filter(pnf=pnf).filter(estado=estado)
                print(103)
          
            elif pnf == "" or pnf == "---------":
                filtro = Proyecto.objects.filter(responsable=responsable).filter(year=year).filter(estado=estado)
                print(104)
          
            elif responsable == None :
                filtro = Proyecto.objects.filter(pnf=pnf).filter(year=year).filter(estado=estado)
                print(105)
          



            elif estado == "" :
                filtro = Proyecto.objects.filter(responsable=responsable).filter(pnf=pnf).filter(year=year)
                print(106)
        

            else:
                filtro = Proyecto.objects.all()
            
            if estado =="":
                estado = "Todos"

            if responsable ==None:
                responsable = "Todos"
            if year =="0":
                year = "Todos"
            if pnf =="":
                pnf = "Todas"
            
            

            return render(request, self.template_name, {'object_list': filtro, "title":"Proyectos Registrados", "form":reporteForm, "year":year, "estado":estado, "responsable":responsable, "pnf":pnf},  )
        return render(request, self.template_name, {'object_list': self.filtro, "title":"Proyectos Registrados", "form":reporteForm},  )
 
    
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
      # Filtros a#o en curso
        context['proyectYearInCourseAproved'] = self.proyectYearInCourse.filter(estado="Aprobado").count()
        context['proyectYearInCourseNotAproved'] = self.proyectYearInCourse.filter(estado="En Curso").count()
        context['proyectYearInCourseInCourse'] = self.proyectYearInCourse.filter(estado="Reprobado").count()

      # Filtros a#o pasado
        context['proyectPastYearAproved'] = self.proyectPastYear.filter(estado="Aprobado").count()
        context['proyectPastYearNotAproved'] = self.proyectPastYear.filter(estado="En Curso").count()
        context['proyectPastYearInCourse'] = self.proyectPastYear.filter(estado="Reprobado").count()

      # Filtros general
        context['proyectAproved'] = Proyecto.filter(estado="Aprobado").count()
        context['proyectNotAproved'] = Proyecto.filter(estado="En Curso").count()
        context['proyectInCourse'] = Proyecto.filter(estado="Reprobado").count()

    

        return context

