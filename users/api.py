from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework import authentication

from users.permissions import UserPermission
from users.serializer import UserSerializer


class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return


class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission, ]
    authentication_classes = [CsrfExemptSessionAuthentication, ]
