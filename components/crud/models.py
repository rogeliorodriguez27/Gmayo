import random
from datetime import date, datetime, timezone

from django.core.exceptions import ValidationError
from django.db import models
from crum import get_current_user
# Create your models here.
import datetime
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]*$', 'Solo se permiten letras')
alphanumericNumbers = RegexValidator(r'^[0-9a-zA-ZñÑáéíóúÁÉÍÓÚ"\s]*$', 'Solo se permiten caracteres alfanuméricos y comillas (")')
alphanumericNumbersComma = RegexValidator(r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ",0-9 ]+$', 'Solo se permiten caracteres alfanuméricos,comas y comillas (")')

#^[0-9]+([,][0-9]+)?$



class Responsable(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre',  validators=[alphanumeric])
    cedula = models.PositiveIntegerField( verbose_name='Cédula', unique=True,)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Responsable'
        verbose_name_plural = 'Responsables'
        ordering = ['id']

class Caso(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre Completo',  validators=[alphanumericNumbers])
    parroquia = models.CharField(max_length=30,  verbose_name='Parroquia',  validators=[alphanumericNumbers])
    municipio = models.CharField(max_length=30, default='Tucupita', verbose_name='Municipio',  validators=[alphanumeric])
    estado = models.CharField(max_length=30, default='Delta Amacuro', verbose_name="Estado",  validators=[alphanumeric])


    def __str__(self):
        return self.nombre

def file_size(value): # add this to some file where you can import it from
    limit = 5 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('Archivo muy grande, no puede exceder los 5MB.')


class Proyecto(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre',  validators=[alphanumericNumbersComma])

    pnf_choice = [
        ("Administración", "Administración"),
        ("Contaduría Pública", 'Contaduria Pública'),
        ("Turismo", 'Turismo'),
        ("Agroalimentación", 'Agroalimentación'),
        ("Informática", 'Informática'),
        ("Construcción Civil", 'Construcción Civil'),
        ("Procesamiento y Distribución de alimentos", 'Procesamiento y Dist. de alimentos'),
        ("Terapia Ocupacional", 'Terapia Ocupacional'),
        ("Fisioterapia", 'Fisioterapia'),
        ("Medicina Veterinaria", 'Medicina Veterinaria'),
        ("Enfermería Integral Comunitaria", 'Enfermeria Int. Comunitaria'),
        ("Educación Inicial", 'Educación Inicial'),



    ]

    pnf = models.TextField(
        max_length=50,
        choices=pnf_choice,

        verbose_name="Carrera",
        blank=True,
        null = True
    )

    estado_choice = [
        ("Aprobado", "Aprobado"),
        ("En curso", 'En curso'),
        ("Reprobado", 'Reprobado'),
    ]

    estado = models.TextField(
        max_length=20,
        choices=estado_choice,
        verbose_name="Estatus",
        blank=True
    )

    trayecto_choice = [
        ("I", "I"),
        ("II", 'II'),
        ("III", 'III'),
        ("IV", 'IV'),
    ]

    trayecto = models.TextField(
        max_length=3,
        choices=trayecto_choice,
        verbose_name="Trayecto",
        blank=True,
    )

    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    yearToday = date.strftime("%Y")
    yearInt = int(yearToday) + 1
    yearChoice = [(f'{i}',f'{i}') for i in range(2008, yearInt)]

    year = models.CharField(choices=yearChoice,max_length=5, verbose_name="Periodo Académico", blank=True)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE, verbose_name='Responsable', blank=True)
    caso = models.ForeignKey(Caso, on_delete=models.CASCADE, verbose_name='Caso')
    linea = models.CharField(max_length=50, verbose_name='Linea de Investigación', blank=True,  validators=[alphanumeric])
    resumen = models.TextField(max_length=2000, verbose_name='Resumen', default='ninguno',  validators=[alphanumericNumbersComma])

    integrantes = models.TextField(max_length=300, verbose_name='Integrantes', default='no disponible',  validators=[alphanumericNumbersComma])
    upload = models.FileField(max_length=50, upload_to='uploads/%Y/%m/%d/',verbose_name='Documento', blank=True, validators=[file_size])

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['id']

    def save(self, *args, **kwargs):
        user = get_current_user()
        rol = str(user.rol)
        print(rol)
        if rol !="ADMINISTRADOR":
            self.pnf = rol
        self.nombre = self.nombre.upper()
        super(Proyecto, self).save(*args, **kwargs)