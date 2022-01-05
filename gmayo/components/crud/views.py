from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView

from components.crud.forms import ProyectoForm, ResponsableForm, CasoForm
from components.crud.models import Proyecto, Caso, Responsable





class ProyectosCreateView(CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'create.html'
    success_url = reverse_lazy('newResponsable')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir  un Proyecto'
        return context


class ResponsableCreateView(CreateView):
    model = Responsable
    form_class = ResponsableForm
    template_name = 'create.html'
    success_url = reverse_lazy('newProyect')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir  un Responsable'
        return context


class CasoCreateView(CreateView):
    model = Caso
    form_class = CasoForm
    template_name = 'create.html'
    success_url = reverse_lazy('newResponsable')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir  una Caso'
        return context




class ProyectosListView(ListView):
    model = Proyecto
    template_name = "view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Proyectos registrados'


        return context

class CasosListView(ListView):
    model = Caso
    template_name = "view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Casos registrados'


        return context


class ResponsableListView(ListView):
    model = Responsable
    template_name = "view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Responsables registrados'


        return context

class ProyectosUpdateView(UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    success_url = reverse_lazy('proyectos')

    template_name = "create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Proyecto'
        return context

class CasosUpdateView(UpdateView):
    model = Caso
    form_class = CasoForm
    success_url = reverse_lazy('casos')

    template_name = "create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Caso'
        return context

class ResponsableUpdateView(UpdateView):
    model = Responsable
    form_class = ResponsableForm
    success_url = reverse_lazy('responsables')

    template_name = "create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Responsable'
        return context

class ProyectosDeleteView(DeleteView):
    model = Proyecto
    
    success_url = reverse_lazy('proyectos')

    template_name = "create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Proyecto'
        context['text'] = 'Esta seguro de que desea eliminar '
        return context

class CasosDeleteView(DeleteView):
    model = Caso
    
    success_url = reverse_lazy('casos')

    template_name = "create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Caso'
        return context

class ResponsableDeleteView(DeleteView):
    model = Responsable
    success_url = reverse_lazy('responsables')

    template_name = "create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Responsable'
        return context




class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = "detail.html"
