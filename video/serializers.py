from rest_framework.serializers import ModelSerializer
from users.models import User


class VideoSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'video']
