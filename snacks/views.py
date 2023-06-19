from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView,CreateView
from .models import Snack
from django.urls import reverse_lazy
# Create your views here.
class HomePageView(TemplateView):
    template_name="home.html"

class AboutPageView(TemplateView):
    template_name="about.html"

class SnacksListView(ListView):
    template_name="snack_list.html"
    model=Snack
    context_object_name = "snacks"

class SnackDetailsView(DetailView):
    template_name="snack_detail.html"
    model=Snack

class SnackCreateView(CreateView):
    template_name='create_snack.html'
    model=Snack
    fields=  ['name', 'desc', 'desc', 'purchaser']
    # success_url=reverse_lazy('snack_list')