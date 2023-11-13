from django.contrib import admin
from django.urls import path, include
from .views import LandingPageView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name="landing-page"),
    path('leads/', include('leads.urls', namespace="leads")),
    path('login/', LoginView.as_view(), name="login"),
]