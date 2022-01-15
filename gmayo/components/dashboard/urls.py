from django.urls import path

from components.dashboard.views import home, contact

urlpatterns = [
   
    path('', home.as_view(), name='home'),
    path("contacto/", contact.as_view(), name="contact"),

]
