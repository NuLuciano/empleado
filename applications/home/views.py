from django.shortcuts import render
from django.urls import reverse_lazy
#Import Views
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
)
#import models
from .models import Prueba
#Import Forms
from .forms import PruebaForm
# Create your views here.


class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class ResumeFoundationView(TemplateView):
    template_name = 'home/resume_foundation.html'


class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = "ListaNumeros"
    queryset = ["0", "10", "20", "30"]


class ListarPrueba(ListView):
    template_name = "home/listar_prueba.html"
    model = Prueba
    context_object_name = "lista"


class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    success_url = reverse_lazy("home_app:lista_home")
