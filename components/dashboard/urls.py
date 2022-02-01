from django.urls import path

from components.dashboard.views import home, charts

urlpatterns = [
   
    path('', home.as_view(), name='about'),
    path('home', charts.as_view(), name='charts'),
    
]
