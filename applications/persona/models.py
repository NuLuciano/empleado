from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField("Habilidad", max_length=50)

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades empleados"
    
    def __str__(self):
        return str(self.id) + "-" + self.habilidad


class Empleado(models.Model):
    """ modelo para tabla empleado """
    JOB_CHOICES = (
        ("contador", "Contador"),
        ("administrador", "Administrador"),
        ("economista", "Economista"),
        ("otro", "Otro"),
    )
    last_name = models.CharField("Apellidos", max_length=50)
    first_name = models.CharField("Nombres", max_length=50)
    full_name = models.CharField("Nombre completo", max_length=120, blank=True)
    job = models.CharField("Trabajo", max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField("Avatar", upload_to="empleado", blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField("Coloque descripción", blank=True)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ["last_name"]
        unique_together = ("first_name", "departamento")

    def __str__(self):
        return str(self.id) + "-" + self.last_name + "-" + self.first_name