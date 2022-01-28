from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from components.accounts.models import CustomUser


class CreationUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('rol',)
