from django.contrib.auth import login, logout
from rest_framework import views, response, permissions, authentication
from users.serializer import UserSerializer, LoginSerializer


class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return


class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny, ]
    authentication_classes = [CsrfExemptSessionAuthentication, ]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return response.Response(UserSerializer(user).data)


class LogoutView(views.APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, ]

    def post(self, request):
        logout(request)
        return response.Response()
