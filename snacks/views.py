from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Snack

# Create your views here.

class SnackListView(ListView):
    template_name = "snacks/snack_list.html"
    model = Snack

class SnackDetailView(DetailView):
    template_name = "snacks/snack_details.html"
    model = Snack

class SnackCreateView(CreateView):
    template_name = "snacks/snack_create.html"
    model = Snack
    fields = ['name', 'description', 'purchaser']

class SnackUpdateView(UpdateView):
    template_name = "snacks/snack_update.html"
    model = Snack
    fields = ['name', 'description']

class SnackDeleteView(DeleteView):
    template_name = "snacks/snack_delete.html"
    model = Snack
    success_url = reverse_lazy("snack_list")