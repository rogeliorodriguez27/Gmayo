from django.urls import path
from django.contrib.auth.views import LoginView

from .views import SignUpView, UsersListView, UsersUpdateView, logout_view, ProfileUpdateUserView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup', ),
    path('login/', LoginView.as_view(redirect_authenticated_user=True),name='login', ),
    path('profile/', ProfileUpdateUserView.as_view(), name='profile'),
    path('users/', UsersListView.as_view(), name='users'),
    path('edit_user/<int:pk>', UsersUpdateView.as_view(), name='updateUser'),
    path('logout/', logout_view, name='logout'),

]