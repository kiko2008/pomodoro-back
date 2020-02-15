from pomodoro.models import PomodoroConf, PomodoroTask
from rest_framework.viewsets import ModelViewSet

from users.permissions import UserPermission
from pomodoro.serializer import ConfSerializer, TaskSerializer


class PomodoroConfViewSet(ModelViewSet):

    queryset = PomodoroConf.objects.all()
    serializer_class = ConfSerializer
    permission_classes = [UserPermission]


class PomodoroTaskViewSet(ModelViewSet):

    queryset = PomodoroTask.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [UserPermission]
