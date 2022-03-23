from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView 

from .views import SignUpView, UsersListView, UsersUpdateView, logout_view, ProfileUpdateUserView, UserDeleteView

app_name = "accounts"

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup', ),
    path('login/', LoginView.as_view(redirect_authenticated_user=True),name='login', ),
    path('profile/', ProfileUpdateUserView.as_view(), name='profile'),
    path('users/', UsersListView.as_view(), name='users'),
    path('edit_user/<int:pk>', UsersUpdateView.as_view(), name='updateUser'),
    path('delete_user/<int:pk>', UserDeleteView.as_view(), name='deleteUser'),
    path('logout/', logout_view, name='logout'),
    path('password_reset_done/', PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ), name='password_reset_done'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='password_reset_form.html',
         email_template_name="password_reset_email.html",
        success_url=reverse_lazy('accounts:password_reset_done')
    ), name='password_reset'),

    path('password_reset_<uidb64>_<token>/', PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html',
        success_url=reverse_lazy('accounts:password_reset_complete')
    ), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ), name='password_reset_complete'),
]

