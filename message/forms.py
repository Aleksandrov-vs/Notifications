from message.models import Message
from groups.models import Group
from django import forms


class MessageCreationForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(MessageCreationForm, self).__init__(*args, **kwargs)
        self.fields['group'] = forms.ModelChoiceField(Group.objects.filter(manager=user))

    class Meta:
        model = Message
        fields = ['name', 'group', 'file', 'text', 'time']
        error_messages = {
            'name': {
                'max_length': 'Максимальная длина навазания 20 символов'
            },
            'text': {
                'max_length': 'Максимальная длина сообщения 255 символов'
            }
        }

    time = forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'}),
        input_formats=['%d/%m/%Y %H:%M'],
        error_messages={
            'invalid': 'Неверный временной формат'
        })