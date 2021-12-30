from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

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

    def post(self, request, *args, **kwargs):
        super(ProyectosCreateView, self).post(request)
        form = self.get_form()
        form.save()

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
