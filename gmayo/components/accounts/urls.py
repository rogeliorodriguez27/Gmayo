from django.urls import path
from django.contrib.auth.views import LoginView

from .views import SignUpView, logout_view, UpdateUserView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup', ),
    path('login/', LoginView.as_view(redirect_authenticated_user=True),name='login', ),
    path('profile/', UpdateUserView.as_view(), name='profile'),
    path('logout/', logout_view, name='logout'),

]