from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, TemplateView
from weasyprint.fonts import FontConfiguration  # wasypeint 52.5
# from weasyprint.text.fonts import FontConfiguration #weasyprint 54
from components.crud.models import Proyecto, Responsable
from components.reportes.forms import reporteForm

# report
from django.http import HttpResponse, request, HttpResponseRedirect
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile


# Create your views here.

class ReporteProyectosListView(TemplateView):
    template_name = "view.html"
    form_class = reporteForm

    def get_rol(self):
        current_user = self.request.user

        rol = current_user.rol
        rol = str(rol)
        return rol
    def filterQuery(self):
        rol = self.get_rol()
        if rol == "ADMINISTRADOR":
            filtro = Proyecto.objects.all()

        else:
            filtro = Proyecto.objects.filter(pnf=self.get_rol())
        return filtro
    def getPnf(self):
        rol = self.get_rol()
        if rol == "ADMINISTRADOR":
            pnf = "Todas"

        else:
            pnf = rol
        return pnf

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)



    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request.POST)
        rol = self.get_rol()




        if form.is_valid():
            year = form.cleaned_data['years']
            responsable = form.cleaned_data['responsable']
            estado = form.cleaned_data['estado']
            pnf = form.cleaned_data['pnf']
            if rol != "ADMINISTRADOR":
                pnf = ""
            print(pnf)
            if pnf == None:
                pnf = ""
            trayecto = form.cleaned_data['trayecto']


            if estado == "" and responsable == None and year == "0" and pnf == "" and trayecto == "":
                filtro = Proyecto.objects.all()
                pnf = "Todas"

                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                print(1)
                context["pnf"] = pnf
                context["estado"] = "Todos"
                context["responsable"] = "Todos"
                context["year"] = "Todos"
                context["trayecto"] = "Todos"
                context["object_list"] = filtro


            elif estado != "" and responsable != None and year != "0" and pnf != ""and trayecto != "":
                filtro = Proyecto.objects.filter(responsable=responsable).filter(year=year).filter(
                    estado=estado).filter(pnf=pnf).filter(trayecto=trayecto)
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                print(12)
                context["pnf"] = pnf
                context["estado"] = estado
                context["responsable"] = responsable
                context["year"] = year
                context["trayecto"] = trayecto
                context["object_list"] = filtro

            elif estado == "" and responsable != None and year != "0" and pnf != ""and trayecto != "":
                filtro = Proyecto.objects.filter(responsable=responsable).filter(year=year).filter(pnf=pnf).filter(trayecto=trayecto)
                print(3)
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = "Todos"
                context["responsable"] = responsable
                context["year"] = year
                context["trayecto"] = trayecto
                context["object_list"] = filtro

            elif estado != "" and responsable == None and year != "0" and pnf != ""and trayecto != "":
                filtro = Proyecto.objects.filter(estado=estado).filter(year=year).filter(pnf=pnf).filter(trayecto=trayecto)
                print(4)
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = estado
                context["responsable"] = "Todos"
                context["year"] = year
                context["trayecto"] = trayecto
                context["object_list"] = filtro

            elif estado != "" and responsable != None and year == "0" and pnf != ""and trayecto != "":
                filtro = Proyecto.objects.filter(responsable=responsable).filter(estado=estado).filter(pnf=pnf).filter(trayecto=trayecto)
                print(5)
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = estado
                context["responsable"] = responsable
                context["year"] = "Todos"
                context["trayecto"] = trayecto
                context["object_list"] = filtro

            elif estado != "" and responsable != None and year != "0" and pnf == ""and trayecto != "":
                filtro = Proyecto.objects.filter(responsable=responsable).filter(year=year).filter(estado=estado).filter(trayecto=trayecto)
                print(6)
                pnf = "Todos"
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = estado
                context["responsable"] = responsable
                context["year"] = year
                context["trayecto"] = trayecto
                context["object_list"] = filtro

            elif estado != "" and responsable != None and year != "0" and pnf != ""and trayecto == "":
                filtro = Proyecto.objects.filter(responsable=responsable).filter(year=year).filter(pnf=pnf).filter(estado=estado)
                print(7)
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = estado
                context["responsable"] = responsable
                context["year"] = year
                context["trayecto"] = "Todos"
                context["object_list"] = filtro

            elif estado == "" and responsable == None and year != "0" and pnf != ""and trayecto != "":
                filtro = Proyecto.objects.filter(year=year).filter(pnf=pnf).filter(trayecto=trayecto)
                print(8)
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = "Todos"
                context["responsable"] = "Todos"
                context["year"] = year
                context["trayecto"] = trayecto
                context["object_list"] = filtro

            elif estado == "" and responsable != None and year == "0" and pnf != ""and trayecto != "":
                filtro = Proyecto.objects.filter(responsable=responsable).filter(pnf=pnf).filter(trayecto=trayecto)
                print(9)
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = "Todos"
                context["responsable"] = responsable
                context["year"] = "Todos"
                context["trayecto"] = trayecto
                context["object_list"] = filtro

            elif estado == "" and responsable != None and year != "0" and pnf == ""and trayecto != "":
                filtro = Proyecto.objects.filter(responsable=responsable).filter(year=year).filter(trayecto=trayecto)
                print(10)
                pnf = "Todos"
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = "Todos"
                context["responsable"] = responsable
                context["year"] = year
                context["trayecto"] = trayecto
                context["object_list"] = filtro

            elif estado == "" and responsable != None and year != "0" and pnf != ""and trayecto == "":
                filtro = Proyecto.objects.filter(responsable=responsable).filter(year=year).filter(pnf=pnf)
                print(11)
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = "Todos"
                context["responsable"] = responsable
                context["year"] = year
                context["trayecto"] = "Todos"
                context["object_list"] = filtro

            elif estado != "" and responsable == None and year != "0" and pnf != ""and trayecto == "":
                filtro = Proyecto.objects.filter(estado=estado).filter(year=year).filter(pnf=pnf)
                print(12)
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = estado
                context["responsable"] = "Todos"
                context["year"] = year
                context["trayecto"] = "Todos"
                context["object_list"] = filtro


            elif estado != "" and responsable != None and year == "0" and pnf != ""and trayecto == "":
                filtro = Proyecto.objects.filter(estado=estado).filter(responsable=responsable).filter(pnf=pnf)
                print(13)
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = estado
                context["responsable"] = responsable
                context["year"] = "Todos"
                context["trayecto"] = "Todos"
                context["object_list"] = filtro

            elif estado != "" and responsable != None and year != "0" and pnf == ""and trayecto == "":
                filtro = Proyecto.objects.filter(estado=estado).filter(responsable=responsable).filter(year=year)
                print(14)
                pnf = "Todos"
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = estado
                context["responsable"] = "Todos"
                context["year"] = year
                context["trayecto"] = "Todos"
                context["object_list"] = filtro

            elif estado != "" and responsable != None and year == "0" and pnf == ""and trayecto != "":
                filtro = Proyecto.objects.filter(estado=estado).filter(responsable=responsable).filter(trayecto=trayecto)
                print(15)
                pnf = "Todos"
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = estado
                context["responsable"] = responsable
                context["year"] = "Todos"
                context["trayecto"] = trayecto
                context["object_list"] = filtro

            elif estado != "" and responsable == None and year != "0" and pnf == ""and trayecto != "":
                filtro = Proyecto.objects.filter(estado=estado).filter(year=year).filter(trayecto=trayecto)
                print(16)
                pnf = "Todos"
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = estado
                context["responsable"] = "Todos"
                context["year"] = year
                context["trayecto"] = trayecto
                context["object_list"] = filtro

            elif estado != "" and responsable == None and year == "0" and pnf != ""and trayecto != "":
                filtro = Proyecto.objects.filter(estado=estado).filter(pnf=pnf).filter(trayecto=trayecto)
                print(17)
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = estado
                context["responsable"] = "Todos"
                context["year"] = "Todos"
                context["trayecto"] = trayecto
                context["object_list"] = filtro

            elif estado == "" and responsable == None and year == "0" and pnf != ""and trayecto != "":
                filtro = Proyecto.objects.filter(pnf=pnf).filter(trayecto=trayecto)
                print(18)
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = "Todos"
                context["responsable"] = "Todos"
                context["year"] = "Todos"
                context["trayecto"] = trayecto
                context["object_list"] = filtro

            elif estado != "" and responsable == None and year == "0" and pnf == ""and trayecto != "":
                filtro = Proyecto.objects.filter(estado=estado).filter(trayecto=trayecto)
                print(19)
                pnf = "Todos"
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = estado
                context["responsable"] = "Todos"
                context["year"] = "Todos"
                context["trayecto"] = trayecto
                context["object_list"] = filtro

            elif estado != "" and responsable != None and year == "0" and pnf == ""and trayecto == "":
                filtro = Proyecto.objects.filter(estado=estado).filter(responsable=responsable)
                print(20)
                pnf = "Todos"
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = estado
                context["responsable"] = responsable
                context["year"] = "Todos"
                context["trayecto"] = "Todos"
                context["object_list"] = filtro

            elif estado == "" and responsable == None and year != "0" and pnf == ""and trayecto != "":
                filtro = Proyecto.objects.filter(year=year).filter(trayecto=trayecto)
                print(21)
                pnf = "Todos"
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = "Todos"
                context["responsable"] = "Todos"
                context["year"] = year
                context["trayecto"] = trayecto
                context["object_list"] = filtro

            elif estado == "" and responsable != None and year == "0" and pnf != ""and trayecto == "":
                filtro = Proyecto.objects.filter(pnf=pnf).filter(responsable=responsable)
                print(22)
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = "Todos"
                context["responsable"] = responsable
                context["year"] = "Todos"
                context["trayecto"] = "Todos"
                context["object_list"] = filtro

            elif estado == "" and responsable != None and year != "0" and pnf == ""and trayecto == "":
                filtro = Proyecto.objects.filter(year=year).filter(responsable=responsable)
                print(23)
                pnf = "Todos"
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = "Todos"
                context["responsable"] = responsable
                context["year"] = year
                context["trayecto"] = "Todos"
                context["object_list"] = filtro

            elif estado != "" and responsable == None and year != "0" and pnf == ""and trayecto == "":
                filtro = Proyecto.objects.filter(year=year).filter(estado=estado)
                print(24)
                pnf = "Todos"
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = estado
                context["responsable"] = "Todos"
                context["year"] = year
                context["trayecto"] = "Todos"
                context["object_list"] = filtro

            elif estado != "" and responsable == None and year == "0" and pnf != ""and trayecto == "":
                filtro = Proyecto.objects.filter(pnf=pnf).filter(estado=estado)
                print(25)
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = estado
                context["responsable"] = "Todos"
                context["year"] = "Todos"
                context["trayecto"] = "Todos"
                context["object_list"] = filtro

            elif estado == "" and responsable != None and year == "0" and pnf == ""and trayecto != "":
                filtro = Proyecto.objects.filter(responsable=responsable).filter(trayecto=trayecto)
                print(26)
                pnf = "Todos"
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = "Todos"
                context["responsable"] = responsable
                context["year"] = "Todos"
                context["trayecto"] = trayecto
                context["object_list"] = filtro


            elif estado != "" and responsable == None and year == "0" and pnf == ""and trayecto == "":
                filtro = Proyecto.objects.filter(estado=estado)
                print(26)
                pnf = "Todos"
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = estado
                context["responsable"] = "Todos"
                context["year"] = "Todos"
                context["trayecto"] = "Todos"
                context["object_list"] = filtro

            elif estado == "" and responsable != None and year == "0" and pnf == ""and trayecto == "":
                filtro = Proyecto.objects.filter(responsable=responsable)
                print(27)
                pnf = "Todos"
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = "Todos"
                context["responsable"] = responsable
                context["year"] = "Todos"
                context["trayecto"] = "Todos"
                context["object_list"] = filtro

            elif estado == "" and responsable == None and year != "0" and pnf == ""and trayecto == "":
                filtro = Proyecto.objects.filter(year=year)
                pnf = "Todos"
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()
                print(28)
                context["pnf"] = pnf
                context["estado"] = "Todos"
                context["responsable"] = "Todos"
                context["year"] = year
                context["trayecto"] = "Todos"
                context["object_list"] = filtro

            elif estado == "" and responsable == None and year == "0" and pnf != ""and trayecto == "":
                filtro = Proyecto.objects.filter(pnf=pnf)
                print(29)
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = "Todos"
                context["responsable"] = "Todos"
                context["year"] = "Todos"
                context["trayecto"] = "Todos"
                context["object_list"] = filtro

            elif estado == "" and responsable == None and year == "0" and pnf == ""and trayecto != "":
                filtro = Proyecto.objects.filter(trayecto=trayecto)
                print(30)
                pnf = "Todos"
                if rol != "ADMINISTRADOR":
                    filtro = filtro.filter(pnf=self.get_rol())
                    pnf = self.get_rol()

                context["pnf"] = pnf
                context["estado"] = "Todos"
                context["responsable"] = "Todos"
                context["year"] = "Todos"
                context["trayecto"] = trayecto
                context["object_list"] = filtro

            else:
                filtro = self.filterQuery()
                context["object_list"] = filtro
                print(99)




        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gmayo: Proyectos registrados'
        context['title2'] = 'Proyectos'
        context['title3'] = 'Proyectos registrados'
        context['form'] = reporteForm
        context["object_list"] = self.filterQuery()
        context['urlEdit'] = 'edit_proyecto'
        context['urlDelete'] = 'delete_proyecto'
        context["pnf"] = self.getPnf()
        context["estado"] = "Todos"
        context["responsable"] = "Todos"
        context["year"] = "Todos"
        context["trayecto"] = "Todos"

        return context




def generate_pdf(request, pk):
    """Generate pdf."""
    # Model data

    if request.user.is_authenticated:
        objects = Proyecto.objects.filter(id=pk)
        context = {'objects': objects, 'request': request}
        html = render_to_string("detReporte.html", context)
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = "inline; reporte.pdf"
        font_config = FontConfiguration()
        HTML(string=html).write_pdf(response, font_config=font_config)
        return response
    else:
        return HttpResponseRedirect(reverse_lazy('login'))

