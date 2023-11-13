from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    return render(request, 'index.html')

######### Class based views ##########
class LandingPageView(TemplateView):
    template_name = "landing-page.html"