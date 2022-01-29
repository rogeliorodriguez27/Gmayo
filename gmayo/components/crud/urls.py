from django.urls import path
from django.views.generic.edit import BaseUpdateView


from .views import CasosDeleteView, CasosListView, CasosUpdateView, ProyectosCreateViewForNonSuperUser, ProyectosCreateView, ProyectosDeleteView, ProyectosUpdateView, ResponsableCreateView, CasoCreateView, ProyectosListView, ResponsableDeleteView, ResponsableListView, ResponsableUpdateView, ProyectoDetailView

urlpatterns = [
    path('agregar/', ProyectosCreateView.as_view(), name='newProyect'),
    path('agregarProyecto/', ProyectosCreateViewForNonSuperUser.as_view(), name='newProyect'),
    path('agregarCaso/', CasoCreateView.as_view(), name='newCase'),
    path('agregarResponsable/', ResponsableCreateView.as_view(), name='newResponsable'),

    path('proyectos/', ProyectosListView.as_view(), name='proyectos'),
    path('casos/', CasosListView.as_view(), name='casos'),
    path('responsables/', ResponsableListView.as_view(), name='responsables'),



    path('edit_proyecto/<int:pk>', ProyectosUpdateView.as_view(), name='editProyect'),
    path('edit_caso/<int:pk>', CasosUpdateView.as_view(), name='editCase'),
    path('edit_responsable/<int:pk>', ResponsableUpdateView.as_view(), name='editResponsable'),

    path('delete_proyecto/<int:pk>', ProyectosDeleteView.as_view(), name='deleteProyect'),
    path('delete_caso/<int:pk>', CasosDeleteView.as_view(), name='deleteCase'),
    path('delete_responsable/<int:pk>', ResponsableDeleteView.as_view(), name='deleteResponsable'),

    path('detailProyecto/<int:pk>', ProyectoDetailView.as_view(), name='proyectoDetail'),

]
