from django.shortcuts import render, redirect, reverse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.core.mail import send_mail

######### Function based views ##########
def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    
    return render(request, 'leads/lead_list.html', context)

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    return render(request, 'leads/lead_detail.html', {"lead": lead})

# Form creation from model
def lead_create(request):
    form = LeadModelForm()
    if(request.method == 'POST'):
        print('Receiving a post request')
        form = LeadModelForm(request.POST)
        if form.is_valid():
            # This does everything!
            form.save()
            return redirect('/leads')
    context = {
        'form': form
    }
    return render(request, 'leads/lead_create.html', context)

# Form creation semi-manually
def lead_create_manually(request):
    form = LeadForm()
    if(request.method == 'POST'):
        print('Receiving a post request')
        form = LeadForm(request.POST)
        if form.is_valid():
            print("The form is valid")
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age = age,
                agent = agent
            )
            print("Lead has been created")
            return redirect('/leads')
    context = {
        'form': form
    }
    return render(request, 'leads/lead_create.html', context)

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if(request.method == "POST"):
        form = LeadModelForm(request.POST, instance=lead)
        if(form.is_valid()):
            form.save()
            return redirect('/leads')
    return render(request, 'leads/lead_update.html', {"lead": lead, "form": form})

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')

######### Class based views ##########
class LangingPageView(TemplateView):
    template_name = "landing.html"
    
class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"
    
class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"
    
class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads:lead-list")
    
    # Override the form_valid method
    def form_valid(self, form):
        # Send Email
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email="test@test.com",
            recipient_list=["sid@onlysid.com"]
        )
        return super(LeadCreateView, self).form_valid(form)
    
    
class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads:lead-list")
    
class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()
    
    def get_success_url(self):
        return reverse("leads:lead-list")