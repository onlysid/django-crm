from django.shortcuts import render
from .models import Lead

# Function based views
def home_page(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    
    return render(request, 'leads/home_page.html', context)