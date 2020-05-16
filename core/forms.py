from django.forms import ModelForm
from users.models import User
class FormReg(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']