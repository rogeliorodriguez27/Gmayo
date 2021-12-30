from django.urls import path

from .views import ProyectosCreateView, ResponsableCreateView, CasoCreateView

urlpatterns = [
    path('agregar/', ProyectosCreateView.as_view(), name='newProyect'),
    path('agregarCaso/', CasoCreateView.as_view(), name='newCase'),
    path('agregarResponsable/', ResponsableCreateView.as_view(), name='newResponsable'),
]
