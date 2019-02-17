from django.contrib.auth import get_user_model
# Create your views here.
from rest_framework import permissions, parsers, renderers
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.authuser.serializers import UserSerializer

User = get_user_model()


class CreateUserView(CreateAPIView):
    permission_classes = [
        permissions.AllowAny,
        # Or anon users can't register
    ]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class Login(APIView):
    throttle_classes = ()
    permission_classes = ()
    queryset = User.objects.all()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        serialized_profile = UserSerializer(user)
        return Response(serialized_profile.data)
