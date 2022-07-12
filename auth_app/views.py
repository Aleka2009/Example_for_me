from rest_framework import views, response, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_app.models import MyUser
from auth_app.serializers import UserSerializer


class UserRegisterAPIViews(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""ПРОВЕРКА ЛОГИНА И ПАРОЛЯ. ВРУЧНУЮ"""


class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        login = request.data.get('username')
        if not MyUser.objects.filter(username=login).exists():
            return Response(
                f'{login} - does not exists'
            )
        user = MyUser.objects.get(username=login)
        password = request.data.get('password')
        pass_check = user.check_password(password)
        if not pass_check:
            return Response('login or password incorrect')
        token = Token.objects.get(user=user)
        return Response({'token': str(token.key)})
