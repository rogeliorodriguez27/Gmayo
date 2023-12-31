from django.contrib.auth.models import AbstractUser
from django.db import IntegrityError, models


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
        ("Educación Inicial", 'Educación Inicial'),


    ]

    rol = models.CharField(
        max_length=50,
        choices=rol_choice,
        verbose_name="Rol",
        unique=True,
        blank=False
    )
    
    def save(self, *args, **kwargs):
        if self.rol =="":
            try:
                self.rol = "ADMINISTRADOR"
                super(CustomUser, self).save(*args, **kwargs)
            except IntegrityError:
                print("Error: Ya existe un superusuario")
                exit()
                
        else:
            super(CustomUser, self).save(*args, **kwargs)
