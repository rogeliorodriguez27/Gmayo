from django.urls import path
from .views import ReporteProyectosListView
urlpatterns = [
    path('proyectos/', ReporteProyectosListView.as_view(), name='reportProyecto'),]