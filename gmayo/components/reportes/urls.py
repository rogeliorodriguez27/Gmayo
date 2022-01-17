from django.urls import path
from .views import ReporteProyectosListView, generate_pdf
urlpatterns = [
    path('proyectos/', ReporteProyectosListView.as_view(), name='reportProyecto'),
    
    path('detailProyecto/<int:pk>', generate_pdf, name='detailReport'),]