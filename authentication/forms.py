from django.contrib.auth.password_validation import validate_password
from users.models import User
from django import forms
from django.contrib.auth.forms import PasswordChangeForm


class SingUpForm(forms.ModelForm):

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError(u'Пользователь с таким email уже существует')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            validate_password(password)
        except forms.ValidationError:
            raise forms.ValidationError('Придумайте пароль длинной от 8 символов, пароль не должен быть простым')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError(u'Пароли не совпадают')
        return password

    def save(self, commit=True):
        user = super(SingUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['email']
        error_messages = {
            'email': {
                'invalid': 'Введите существующий адрес электронной почты'
            }
        }


class ChangePasswordForm(PasswordChangeForm):

    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(u'Старый пароль неверен')
        return old_password

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(u'Пароли не совпадают')
        return password2
