from datetime import date, datetime, timezone

from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
import datetime





class Responsable(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Responsable'
        verbose_name_plural = 'Responsables'
        ordering = ['id']


class Caso(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    parroquia = models.CharField(max_length=200,  verbose_name='Parroquia')
    municipio = models.CharField(max_length=200, default='Tucupita', verbose_name='Municipio')
    estado = models.CharField(max_length=200, default='Delta Amacuro', verbose_name="Estado")


    class Meta:
       verbose_name = 'Ubicacion'
       verbose_name_plural = 'Ubicaciones'
       ordering = ['id']


class Proyecto(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre')


    estado_choice = [
        ("Aprobado", "Aprobado"),
        ("En curso", 'En curso'),
        ("Reprobado", 'Reprobado'),

    ]


    pnf = models.CharField(max_length=200, verbose_name='Carrera')

    estado = models.CharField(
        max_length=10,
        choices=estado_choice,
        default="Aprobado",
    )

    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    yearToday = date.strftime("%Y")
    yearInt = int(yearToday)



    year = models.IntegerField(choices=[(i, i) for i in range(1984, yearInt)], blank=True)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE, verbose_name='Responsable')
    caso = models.ForeignKey(Caso, on_delete=models.CASCADE, verbose_name='Caso')
    resumen = models.CharField(max_length=300, verbose_name='Resumen', default='ninguno')

    integrantes = models.CharField(max_length=300, verbose_name='Integrantes', default='no disponible')
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)

    user = models.CharField(max_length=300,)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['id']

