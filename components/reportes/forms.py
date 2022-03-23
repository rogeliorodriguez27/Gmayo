import datetime
from django.forms import *
from components.crud.models import Proyecto


class reporteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control form-control-sm'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        #self.fields['responsable'].widget.attrs['required'] = False


    
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    yearToday = date.strftime("%Y")
    yearInt = int(yearToday)
    yearChoice = [(i,i) for i in range(2008, yearInt)]
    yearChoice.insert(0, (0, '----'))

    years = ChoiceField(required=False, choices=yearChoice, label="Periodo Académico")    

    class Meta:
        model = Proyecto
        fields = ("pnf", "responsable",  "trayecto","years", "estado")
        