from django.contrib import admin
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path('prueba/', views.PruebaView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('listar_prueba/', views.ListarPrueba.as_view(), name="lista_home"),
    path('add/', views.PruebaCreateView.as_view()),
    path(
        'resume-foundation/',
        views.ResumeFoundationView.as_view(),
        name="resume_foundation",
    ),
]