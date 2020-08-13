from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import Departamento
from django.views.generic import (
    ListView,
)
# Create your views here.


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = "departamento"
    paginate_by = 5

    def get_queryset(self):
        dpto = self.request.GET.get("kword", "")
        lista = Departamento.objects.filter(
            name__icontains=dpto
    )
        return lista



class NewDepartamentoView(FormView):
    template_name = "departamento/new_departamento.html"
    form_class = NewDepartamentoForm
    success_url = "."

    def form_valid(self, form):
        depa = Departamento(
            name=form.cleaned_data["departamento"],
            shor_name=form.cleaned_data["shorname"],
        )
        depa.save()

        nombre = form.cleaned_data["nombre"]
        apellido = form.cleaned_data["apellido"]
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job="administrador",
            departamento=depa,
        )
        return super(NewDepartamentoView, self).form_valid(form)