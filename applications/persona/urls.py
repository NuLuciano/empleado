from django.contrib import admin
from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
    path(
        '',
        views.InicioView.as_view(),
        name="inicio",
    ),
    path(
        'listar-todos-empleados/',
        views.ListAllEmpleados.as_view(),
        name="lista_empleados",
    ),
    path(
        'listar-todos-empleados-admin/',
        views.ListAllEmpleadosAdmin.as_view(),
        name="lista_empleados_admin",
    ),
    path(
        'lista-por-departamento/<name>/',
        views.ListByAreaEmpleado.as_view(),
        name="filtro_departamento",
    ),
    path(
        'buscar-empleado/',
        views.ListEmpleadoByKword.as_view(),
        name="buscar_empleado",
    ),
    path(
        'buscar-por-trabajo/',
        views.ListByJob.as_view(),
        name="buscar_por_trabajo",
    ),
    path(
        'buscar-por-habilidades/',
        views.ListHabilidadesEmpleado.as_view(),
        name="buscar_por_habilidades",
    ),
    path(
        'ver-empleado/<pk>/',
        views.EmpleadoDetailView.as_view(),
        name="detalle_empleado",
    ),
    path(
        'add-empleado/',
        views.EmpleadoCreateView.as_view(),
        name="agregar_empleado"
    ),
    path(
        'success/',
        views.SuccessView.as_view(),
        name="correcto",
    ),
    path(
        'update-empleado/<pk>/',
        views.EmpleadoUpdateView.as_view(),
        name="modificar_empleado",
    ),
    path(
        'delete-empleado/<pk>/',
        views.EmpleadoDeleteView.as_view(),
        name="eliminar_empleado",
    ),
]