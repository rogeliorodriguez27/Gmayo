from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout
from django.views.generic.edit import DeleteView, UpdateView

from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User, AnonymousUser

from components.accounts.forms import CreationUserForm, ProfileForm

from components.accounts.models import CustomUser



class SignUpView(generic.CreateView):
    form_class = CreationUserForm
    success_url = reverse_lazy('accounts:users')
    template_name = 'create.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.rol !="ADMINISTRADOR" :
            return redirect(reverse_lazy('charts'))
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gmayo: Crear Usuario'
        context['title2'] = 'Usuario'
        context['cardTitle'] = 'Crear Usuario'

        return context

class ProfileUpdateUserView(generic.UpdateView):
    form_class = ProfileForm

    success_url = reverse_lazy('charts')
    template_name = 'create.html'
    model = CustomUser

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        user = self.request.user
        return user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gmayo: Perfil'
        context['title2'] = 'Perfil'
        context['cardTitle'] = 'Datos del Perfil'

        return context

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse_lazy('about'))

class UsersListView(generic.ListView):
    model = CustomUser
    template_name = "view.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.rol != "ADMINISTRADOR":
            return HttpResponseRedirect(reverse_lazy('charts'))


        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gmayo: Usuarios registrados'
        context['urlEdit'] = '/accounts/edit_user'
        context['urlDelete'] = '/accounts/delete_user'
        context['title2'] = 'Usuarios'
        context['cardTitle'] = 'Usuarios Registrados'

        return context

class UsersUpdateView(UpdateView):
    model = CustomUser
    form_class = CreationUserForm
    success_url = reverse_lazy('accounts:users')

    template_name = "create.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.rol != "ADMINISTRADOR":
            return redirect(reverse_lazy('charts'))

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Gmayo: Editar Usuario'
        context['title2'] = 'Usuarios'
        context['cardTitle'] = 'Editar Usuarios'

        return context


class UserDeleteView(DeleteView):
    model = CustomUser
    success_url = reverse_lazy('accounts:users')

    template_name = "create.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.rol != "ADMINISTRADOR":
            return redirect(reverse_lazy('charts'))

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Usuario'
        context['text'] = 'Esta seguro de que desea eliminar este usuario'
        context['title2'] = 'Usuario'
        context['cardTitle'] = 'Eliminar Usuario'

        return context

