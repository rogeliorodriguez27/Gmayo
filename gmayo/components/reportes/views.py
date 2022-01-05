from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from components.crud.models import Proyecto, Responsable
from components.reportes.forms import reporteForm

# Create your views here.

class ReporteProyectosListView(ListView):
    model = Proyecto
    template_name = "view.html"
    form_class = reporteForm  
    filtro = Proyecto.objects.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Proyectos registrados'
        context['form'] = reporteForm


        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            responsable = form.cleaned_data['responsable']
            estado = form.cleaned_data['estado']
            if year !="":
                if responsable !="":
                    filtro = Proyecto.objects.filter(year=year).filter(responsable=responsable)
                elif estado !="--------":
                    filtro = Proyecto.objects.filter(year=year).filter(estado=estado)
 











            else:
                filtro = Proyecto.objects.all()
            return render(request, self.template_name, {'object_list': filtro, "title":"Proyectos Registrados", "form":reporteForm},  )
        return render(request, self.template_name, {'object_list': self.filtro, "title":"Proyectos Registrados", "form":reporteForm},  )










    