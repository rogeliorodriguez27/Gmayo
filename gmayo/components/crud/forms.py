from django.forms import ModelForm, TextInput, forms
from components.crud.models import Proyecto, Caso, Responsable


class ProyectoForm(ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
        exclude = ('user',)

class CasoForm(ModelForm):
    class Meta:
        model = Caso
        fields = '__all__'

class ResponsableForm(ModelForm):
    class Meta:
        model = Responsable
        fields = '__all__'
