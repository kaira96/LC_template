from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .models import Lead
from .forms import LeadForm
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def services(request):
    return render(request, 'website/services.html')

def team(request):
    return render(request, 'website/team.html')

def contact(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            leads = form.save()
            return redirect('/')
    else:
        form = LeadForm()
    return render(request, 'website/contact.html', {'form' : form})
