from users.models import User
from django import forms
from django.contrib.auth.forms import PasswordChangeForm


class SignupForm(forms.ModelForm):

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        cd = self.cleaned_data
        email = cd['email']
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError(u'Пользователь с таким email уже существует')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(u'Пароли не совпадают')
        return password1

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class ChangePasswordForm(PasswordChangeForm):

    def clean_old_password(self):

        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(u'старый пароль неверен')
        return old_password

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(u'Пароли не совпадают')
        return password2
