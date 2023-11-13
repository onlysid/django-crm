from django.urls import path
from .views import LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView, LeadListView

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name="lead-list"),
    path('create/', LeadCreateView.as_view(), name="lead-create"),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name="lead-delete"),
    path('<int:pk>/update', LeadUpdateView.as_view(), name='lead-update'),
]
