from django.forms import *
from components.crud.models import Proyecto


class chartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        #self.fields['responsable'].widget.attrs['required'] = False


    class Meta:
        model = Proyecto
        fields = ("pnf",)
        