from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import VideoSerializer
from rest_framework.permissions import IsAuthenticated
from users.models import User
from rest_framework.views import csrf_exempt


class VideoApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user
        email = user.email
        video = user.video
        # data = {'email': email,
        #         'video': video
        #         }
        # serializer = VideoSerializer(data=data)
        # serializer.is_valid(raise_exception=True)
        return Response({'response': user.video.url})

    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(email=request.email)
        return Response({'video_url': user.video.url})
