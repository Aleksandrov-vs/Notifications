from rest_framework import serializers
from users.models import User
from django.contrib.auth.password_validation import validate_password


class SingUpSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(label='Подтверждение пароля', style={'input_type': 'password'}, write_only=True)

    def validate_email(self, value):
        email = value
        if email and User.objects.filter(email=email).exists():
            raise serializers.ValidationError(u'Пользователь с таким email уже существует')
        return email

    def validate_password(self, value):

        if validate_password(value) is not None:
            raise serializers.ValidationError('Придумайте пароль длинной от 8 символов, пароль не должен быть простым')
        return value

    def validate_password2(self, value):
        print('password2= ', value)
        if len(value) < 1:
            raise serializers.ValidationError('пароли несовпадают')
        return value



    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
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
        validators: []
        extra_kwargs = {
            'email': {
                'validators': [],
                "error_messages": {
                    'non_field_errors': ' ничего не работает ',
                    "required": "это поле обязательно.",
                    "null": "это поле не может быть null.",
                    "invalid": "Введите существующий адрес электронной почты",
                    'unique': 'пользователь с таким именнем уже есть'
                }
            },
            'password': {
                'validators': [],
                'write_only': True,
                'error_messages': {
                        'non_field_errors"': ' ничего не работает ',
                        'invalid': 'Придумайте пароль длинной от 8 символов, пароль не должен быть простым',
                        'required': 'поле не должно быть пустым',
                        'null': 'поле не должно быть пустым'
                    }
            }
        }


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(label='email')
    password = serializers.CharField(label='Подтверждение пароля', style={'input_type': 'password'}, write_only=True)

    def len_null(self, value):
        if len(value) == 0:
            return True
        return False

    def validate_email(self, value):
        if self.len_null(value):
            print('поле не должно быть пустым')
            raise serializers.ValidationError('поле не должно быть пустым')
        return value

    def validate_password(self, value):
        if self.len_null(value):
            print('поле не должно быть пустым')
            raise serializers.ValidationError('поле не должно быть пустым')
        return value

    def validate(self, attrs):

        email = attrs['email']
        password = attrs['password']

        try:
            u = User.objects.get(email=email)
        except Exception:
            raise serializers.ValidationError('email или пароль не верны')

        if not (u.check_password(password)):
            raise serializers.ValidationError('email или пароль не верны')

        return attrs
