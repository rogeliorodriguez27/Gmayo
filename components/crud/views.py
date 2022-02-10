from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView

from components.crud.forms import ProyectoForm, ResponsableForm, CasoForm, ProyectoFormForNonSuperUser
from components.crud.models import Proyecto, Caso, Responsable



class ProyectosCreateView(CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'create.html'
    success_url = reverse_lazy('reportProyecto')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.rol == "Coord. Proyectos":
            return redirect(reverse_lazy('charts'))

        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gmayo: Añadir  un Proyecto'
        context['title2'] = 'Proyectos'
        context['cardTitle'] = 'Añadir un Proyecto'
        return context

class ProyectosCreateViewForNonSuperUser(CreateView):
    model = Proyecto
    form_class = ProyectoFormForNonSuperUser
    template_name = 'create.html'
    success_url = reverse_lazy('reportProyecto')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.rol == "Coord. Proyectos":
            return redirect(reverse_lazy('charts'))

        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gmayo: Añadir  un Proyecto'
        context['title2'] = 'Proyectos'
        context['cardTitle'] = 'Añadir un Proyecto'
        return context


class ResponsableCreateView(CreateView):
    model = Responsable
    form_class = ResponsableForm
    template_name = 'create.html'
    success_url = reverse_lazy('responsables')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.rol == "Coord. Proyectos":
            return redirect(reverse_lazy('charts'))

        return super().dispatch(request, *args, **kwargs)



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gmayo: Añadir  un Docente'
        context['title2'] = 'Docentes'
        context['cardTitle'] = 'Añadir un Docente'

        return context


class CasoCreateView(CreateView):
    model = Caso
    form_class = CasoForm
    template_name = 'create.html'
    success_url = reverse_lazy('casos')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.rol == "Coord. Proyectos":
            return redirect(reverse_lazy('charts'))

        return super().dispatch(request, *args, **kwargs)



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gmayo: Añadir  una Caso'
        context['title2'] = 'Casos'
        context['cardTitle'] = 'Añadir un Caso'

        return context







class CasosListView(ListView):
    model = Caso
    template_name = "view.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gmayo: Casos registrados'
        context['urlEdit'] = '/crud/edit_caso'
        context['urlDelete'] = '/crud/delete_caso'
        context['title2'] = 'Casos'
        context['cardTitle'] = 'Casos Registrados'

        return context


class ResponsableListView(ListView):
    model = Responsable
    template_name = "view.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gmayo: Responsables registrados'
        context['urlEdit'] = '/crud/edit_responsable'
        context['urlDelete'] = '/crud/delete_responsable'
        context['title2'] = 'Responsables'
        context['cardTitle'] = 'Responsables registrados'

        return context

class ProyectosUpdateView(UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    success_url = reverse_lazy('reportProyecto')

    template_name = "create.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.rol == "Coord. Proyectos":
            return redirect(reverse_lazy('charts'))

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gmayo: Editar Proyecto'
        context['title2'] = 'Proyectos'
        context['cardTitle'] = 'Editar Proyecto'
        return context

class CasosUpdateView(UpdateView):
    model = Caso
    form_class = CasoForm
    success_url = reverse_lazy('casos')

    template_name = "create.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.rol == "Coord. Proyectos":
            return redirect(reverse_lazy('charts'))

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gmayo: Editar Caso'
        context['title2'] = 'Casos'
        context['cardTitle'] = 'Editar Caso'

        return context

class ResponsableUpdateView(UpdateView):
    model = Responsable
    form_class = ResponsableForm
    success_url = reverse_lazy('responsables')

    template_name = "create.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.rol == "Coord. Proyectos":
            return redirect(reverse_lazy('charts'))

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gmayo: Editar Responsable'
        context['title2'] = 'Responsable'
        context['cardTitle'] = 'Editar Responsable'

        return context

class ProyectosDeleteView(DeleteView):
    model = Proyecto
    
    success_url = reverse_lazy('reportProyecto')

    template_name = "create.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.rol == "Coord. Proyectos":
            return redirect(reverse_lazy('charts'))

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Proyecto'
        context['text'] = 'Esta seguro de que desea eliminar '
        context['title2'] = 'Proyectos'
        context['cardTitle'] = 'Eliminar Proyecto'

        return context

class CasosDeleteView(DeleteView):
    model = Caso
    
    success_url = reverse_lazy('casos')

    template_name = "create.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.rol == "Coord. Proyectos":
            return redirect(reverse_lazy('charts'))

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Caso'
        context['text'] = 'Esta seguro de que desea eliminar '
        context['title2'] = 'Casos'
        context['cardTitle'] = 'Eliminar Caso'

        return context

class ResponsableDeleteView(DeleteView):
    model = Responsable
    success_url = reverse_lazy('responsables')

    template_name = "create.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.rol == "Coord. Proyectos":
            return redirect(reverse_lazy('charts'))

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Responsable'
        context['text'] = 'Esta seguro de que desea eliminar '
        context['title2'] = 'Responsables'
        context['cardTitle'] = 'Eliminar Responsable'

        return context




class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = "detail.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
       
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gmayo: Detalles del Proyecto'
        context['title2'] = 'Proyectos'
        context['cardTitle'] = 'Detalles del Proyecto: '

        return context
