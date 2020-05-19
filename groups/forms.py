from groups.models import Group
from django import forms


class GroupCreationForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['name']
        error_messages = {
            'name': {
                'max_length': 'Максимальная длина навазания 20 символов'
            }
        }