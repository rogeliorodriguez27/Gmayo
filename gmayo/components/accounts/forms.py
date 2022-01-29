from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, forms, EmailField, CharField

from components.accounts.models import CustomUser


class CreationUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('rol',)


class ProfileForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
#        self.fields['username'].widget.attrs['readonly'] = True

    email = EmailField(required=True)
    first_name = CharField(required=False, label="Nombre")
    last_name = CharField(required=False, label="Apellido")

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name',)
        exclude = ("username",)