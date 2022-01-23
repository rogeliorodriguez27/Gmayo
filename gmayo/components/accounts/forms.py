from django.contrib.auth.forms import UserCreationForm
from django.forms import *
from gmayo.models import Usuario


class customUser(UserCreationForm):
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


   

    pnf = TextField(
        max_length=41,
        choices=pnf_choice,
        default="Aprobado",
        verbose_name="Carrera",
        blank=True
    )

    

    class Meta:
        model = Usuario
        fields = ('username','pnf',)