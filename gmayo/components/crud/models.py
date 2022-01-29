from datetime import date, datetime, timezone

from django.core.exceptions import ValidationError
from django.db import models
from crum import get_current_user
# Create your models here.
import datetime




class Responsable(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Responsable'
        verbose_name_plural = 'Responsables'
        ordering = ['id']


class Caso(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre')
    parroquia = models.CharField(max_length=200,  verbose_name='Parroquia')
    municipio = models.CharField(max_length=200, default='Tucupita', verbose_name='Municipio')
    estado = models.CharField(max_length=200, default='Delta Amacuro', verbose_name="Estado")
    
    
    def __str__(self):
        return self.nombre

def file_size(value): # add this to some file where you can import it from
    limit = 5 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('Archivo muy grande, no puede exceder los 5MB.')


class Proyecto(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre')

    pnf_choice = [
        ("Administracion", "Administracion"),
        ("Contaduria Publica", 'Contaduria Publica'),
        ("Turismo", 'Turismo'),
        ("Agroalimentacion", 'Agroalimentacion'),
        ("Informatica", 'Informatica'),
        ("Construccion Civil", 'Construccion Civil'),
        ("Procesamiento y Distribucion de alimentos", 'Procesamiento y Dist. de alimentos'),
        ("Terapia Ocupacional", 'Terapia Ocupacional'),
        ("Fisioterapia", 'Fisioterapia'),

    ]

    pnf = models.TextField(
        max_length=41,
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
        max_length=50,
        choices=estado_choice,
        verbose_name="Estado",
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
    yearChoice = [(i, i) for i in range(2008, yearInt)]

    year = models.IntegerField(choices=yearChoice, verbose_name="Año", blank=True)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE, verbose_name='Responsable', blank=True)
    caso = models.ForeignKey(Caso, on_delete=models.CASCADE, verbose_name='Caso')
    resumen = models.TextField(max_length=300, verbose_name='Resumen', default='ninguno')

    integrantes = models.TextField(max_length=300, verbose_name='Integrantes', default='no disponible')
    upload = models.FileField(max_length=50, upload_to='uploads/%Y/%m/%d/',verbose_name='Documento', blank=False, validators=[file_size])

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
        super(Proyecto, self).save(*args, **kwargs)