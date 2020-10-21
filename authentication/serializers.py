from rest_framework import serializers
from users.models import User
from django.contrib.auth.password_validation import validate_password


class SingUpSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(label='Подтверждение пароля', style={'input_type': 'password'}, write_only=True)
    def validate_email(self, value):
        email = value
        print('afioajfoiajhfoiafjaifj')
        if email and User.objects.filter(email=email).exists():
            raise serializers.ValidationError(u'Пользователь с таким email уже существует')
        return email

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        print('valid_pass ', validate_password(password))
        try:
            print('valid_pass ', validate_password(password))
            validate_password(password)
        except serializers.ValidationError:
            raise serializers.ValidationError('Придумайте пароль длинной от 8 символов, пароль не должен быть простым')

        if password and password2 and password != password2:
                raise serializers.ValidationError(u'Пароли не совпадают')

        return attrs

    def save(self, **kwargs):
        user = User(email=self.validated_data.get('email'))
        user.set_password(self.validated_data.get('password2'))
        user.save()
        return user

    class Meta:
        model = User
        fields = ['email', 'password', 'password2']
        extra_kwargs = {
            'email': {'error_messages': {'invalid': 'Введите существующий адрес электронной почты'}},
            'password': {'write_only': True}
        }


class LoginSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ['email', 'password']

