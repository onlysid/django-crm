from django.contrib import admin
from django.urls import path, include
from .views import LandingPageView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordChangeDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name="landing-page"),
    path('leads/', include('leads.urls', namespace="leads")),
    path('reset-password/', PasswordResetView.as_view(), name="reset-password"),
    path('password-reset-done/', PasswordChangeDoneView.as_view(), name="password_reset_done"),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('login/', LoginView.as_view(), name="login"),
]