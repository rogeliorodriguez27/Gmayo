from fileinput import FileInput
from datetime import datetime
from django.forms import *
from components.crud.models import Proyecto, Caso, Responsable
from crum import get_current_user


class ProyectoFormForNonSuperUser(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['upload'].widget.attrs['accept'] = 'application/pdf'
        # self.fields['pnf'].initial = "rol"

    class Meta:
        model = Proyecto
        fields = '__all__'
        exclude = ('created_by', "modified_by","pnf")
        widgets = {
            'responsable': Select(
                attrs={
                    'required': True,
                }
            )


            ,
            'trayecto': Select(
                attrs={
                    'required': True,
                }

            ),
            'estado': Select(
                attrs={
                    'required': True,
                }

            )
        }

        def save(self, commit=True):
            self.pnf = "Fisioterapia"

            return super(ProyectoFormForNonSuperUser, self).save(commit=commit)


class ProyectoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['upload'].widget.attrs['accept'] = 'application/pdf'

    class Meta:
        model = Proyecto
        fields = '__all__'
        exclude = ('created_by',"modified_by")
        widgets = {
            'responsable': Select(
                attrs={
                    'required': True,
                }
            ),'pnf': Select(
                attrs={
                    'required': True,
                }


            ),
              'trayecto': Select(
                attrs={
                    'required': True,
                }

                
            ),
              'estado': Select(
                attrs={
                    'required': True,
                }
                
            )
        }

class CasoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Caso
        fields = '__all__'

class ResponsableForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Responsable
        fields = '__all__'
