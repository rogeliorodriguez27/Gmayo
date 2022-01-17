from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from weasyprint.fonts import FontConfiguration
from components.crud.models import Proyecto, Responsable
from components.reportes.forms import reporteForm



#report
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile



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
        context["responsable"] = "Todos"
        context["pnf"] = "Todos"
        context["estado"] = "Todos"
        context["year"] = "Todos"


        return context

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




def generate_pdf(request, pk):
    """Generate pdf."""
    # Model data
    objects = Proyecto.objects.filter(id=pk)

    context = {'objects': objects}
    html = render_to_string("detReporte.html", context)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; reporte.pdf"

    font_config = FontConfiguration()
    HTML(string=html).write_pdf(response, font_config=font_config)

    return response





    