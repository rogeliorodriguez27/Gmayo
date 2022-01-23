from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
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
        blank=True)
