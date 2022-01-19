from datetime import date, datetime, timezone

from django.core.exceptions import ValidationError
from django.db import models
from crum import get_current_user

# Create your models here.
import datetime




class TimeStampMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', blank=True, null=True,
                                   default=None, on_delete=models.CASCADE)
    modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey('auth.User', blank=True, null=True,
                                    default=None, on_delete=models.CASCADE, related_name="modified_by")
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        super(TimeStampMixin, self).save(*args, **kwargs)

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

    class Meta:
       verbose_name = 'Ubicacion'
       verbose_name_plural = 'Ubicaciones'
       ordering = ['id']


class Proyecto(TimeStampMixin):
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
        default="Aprobado",
        verbose_name="Carrera",
        blank=True
    )




    estado_choice = [
        ("Aprobado", "Aprobado"),
        ("En curso", 'En curso'),
        ("Reprobado", 'Reprobado'),
    ]


   

    estado = models.TextField(
        max_length=50,
        choices=estado_choice,
        default="Aprobado",
        verbose_name="Estado",
        blank=True
    )

    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    yearToday = date.strftime("%Y")
    yearInt = int(yearToday)+1
    yearChoice =[(i, i) for i in range(2008, yearInt)]
    


    year = models.IntegerField(choices=yearChoice, verbose_name="Año", blank=True)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE, verbose_name='Responsable', blank=True)
    caso = models.ForeignKey(Caso, on_delete=models.CASCADE, verbose_name='Caso')
    resumen = models.TextField(max_length=300, verbose_name='Resumen', default='ninguno')

    integrantes = models.TextField(max_length=300, verbose_name='Integrantes', default='no disponible')
    upload = models.FileField(max_length=50,upload_to='uploads/%Y/%m/%d/', blank=False, )

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['id']

