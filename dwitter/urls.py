from django.urls import path, include, reverse_lazy
from .views import dashboard, profile_list, profile, register
from django.contrib.auth import views as auth_views

app_name = "dwitter"
urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path("register/", register, name="register"),
    path('accounts/login',
         auth_views.LoginView.as_view(),
         name='login'),
    path('accounts/logout',
         auth_views.LogoutView.as_view(),
         name='logout'),
    path('accounts/password_change/',
         auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('dwitter:password_change_done')),
         name='password_change'),
    path('accounts/password_change_done/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('accounts/passowrd_reset',
         auth_views.PasswordResetView.as_view(success_url=reverse_lazy('dwitter:password_reset_done')),
         name='password_reset'),
    path('accounts/password_reset_done',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('accounts/password_reset_confirm',
         auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('dwitter:password_reset_complete')),
         name='password_reset_confirm'),
    path('accounts/passoword_reset_complete',
         auth_views.PasswordResetCompleteView.as_view(),
         name='passoword_reset_complete'),

]
