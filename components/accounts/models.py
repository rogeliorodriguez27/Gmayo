from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    rol_choice = [
        ("ADMINISTRADOR", "ADMINISTRADOR"),
        ("Administracion", "Coord. Administración"),
        ("Contaduria Publica", 'Coord. Contaduria Publica'),
        ("Turismo", 'Coord.Turismo'),
        ("Agroalimentacion", 'Coord. Agroalimentación'),
        ("Informatica", 'Coord. Informatica'),
        ("Construccion Civil", 'Coord. Construcción Civil'),
        ("P. y D. de alimentos", 'Coord. Proc. y Dist. de alimentos'),
        ("Terapia Ocupacional", 'Coord. Terapia Ocupacional'),
        ("Fisioterapia", 'Coord. Fisioterapia'),

    ]

    rol = models.CharField(
        max_length=23,
        choices=rol_choice,
        verbose_name="Rol",
        unique=True,
    )
