from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    rol_choice = [
        ("ADMINISTRADOR", "ADMINISTRADOR"),
        ("Coord. Proyectos", "Coord. Proyectos"),
        ("Administración", "Coord. Administración"),
        ("Contaduría Pública", 'Coord. Contaduría Pública'),
        ("Turismo", 'Coord.Turismo'),
        ("Agroalimentación", 'Coord. Agroalimentación'),
        ("Informática", 'Coord. Informática'),
        ("Construcción Civil", 'Coord. Construcción Civil'),
        ("Procesamiento y Distribución de alimentos", 'Coord. Proc. y Dist. de alimentos'),
        ("Terapia Ocupacional", 'Coord. Terapia Ocupacional'),
        ("Fisioterapia", 'Coord. Fisioterapia'),
        ("Medicina Veterinaria", 'Coord. Medicina Veterinaria'),
        ("Enfermería Integral Comunitaria", 'Coord. Enfermeria Int.'),


    ]

    rol = models.CharField(
        max_length=50,
        choices=rol_choice,
        verbose_name="Rol",
        unique=True,
    )
