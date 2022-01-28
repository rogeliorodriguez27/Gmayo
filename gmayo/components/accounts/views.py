from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout
from django.views.generic.edit import DeleteView, UpdateView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

from components.accounts.forms import CreationUserForm


class SignUpView(generic.CreateView):
    form_class = CreationUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('about'))

