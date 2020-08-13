from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
from .models import Empleado, Habilidades
# Create your views here.


class InicioView(TemplateView):
    """Pagina de inicio"""
    template_name = "inicio.html"


class ListAllEmpleados(ListView):
    """ Lista de todos los empleados """
    template_name = "persona/list_all.html"
    paginate_by = 5
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", "")
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
    )
        return lista


class ListAllEmpleadosAdmin(ListView):
    """ Lista de todos los empleados """
    template_name = "persona/list_all_admin.html"
    paginate_by = 10
    ordering = 'last_name'
    context_object_name = 'empleados'
    model = Empleado


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = [
        "first_name",
        "last_name",
        "job",
        "departamento",
        "habilidades",
    ]
    success_url = reverse_lazy("persona_app:lista_empleados_admin")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        return super(EmpleadoUpdateView, self).post(request, *args, **kwargs)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy("persona_app:lista_empleados_admin")


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"


class ListByAreaEmpleado(ListView):
    """ Lista empleados por area """
    template_name = "persona/list_by_area.html"
    context_object_name = "area"

    def get_queryset(self):
        area = self.kwargs["name"]
        lista = Empleado.objects.filter(
        departamento__name=area
    )
        return lista


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    fields = [
        "first_name",
        "last_name",
        "job",
        "departamento",
        "habilidades",
        "avatar",
    ]
    success_url = reverse_lazy("persona_app:correcto")

    def form_valid(self, form):
        #Logica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + " " + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


    # 1. Lista todos los empleados de la empresa
    # 2. Listar todos los empleados que pertenecen a un area de la empresa
    # 3. Listar empleados por trabajo
    # 4. Listar los empleados por palabra clave
    # 5. Listar habilidades de un empleado


class ListByJob(ListView):
    """Lista empleados por trabajo"""
    template_name = "persona/by_job.html"
    context_object_name = "empleados"

    def get_queryset(self):
        job_key = self.request.GET.get("jkey",)
        lista = Empleado.objects.filter(
            job=job_key
    )
        return lista


class ListEmpleadoByKword(ListView):
    """ Lista empleados por palabra clave """
    template_name = "persona/by_kword.html"
    context_object_name = "empleados"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", "")
        lista = Empleado.objects.filter(
        first_name=palabra_clave
    )
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = "persona/por_habilidades.html"
    context_object_name = "habilidades"


    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", int(1))
        empleado = Empleado.objects.get(id=palabra_clave)
        return empleado.habilidades.all()

        # empleado = Empleado.objects.get(id=8)
        # return empleado.habilidades.all()



class SuccessView(TemplateView):
    template_name = "persona/success.html"

