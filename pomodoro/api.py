from pomodoro.models import PomodoroConf, PomodoroTask
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from users.permissions import UserPermission
from pomodoro.serializer import ConfSerializer, TaskSerializer


class PomodoroConfViewSet(ModelViewSet):

    queryset = PomodoroConf.objects.all()
    serializer_class = ConfSerializer
    permission_classes = [UserPermission]

    def retrieve(self, request):
        username = request.query_params['username']
        conf_by_user_queryset = PomodoroConf.objects.filter(user_id=2).order_by('-pub_date')
        serializer = ConfSerializer(conf_by_user_queryset)
        return Response(serializer.data)

class PomodoroTaskViewSet(ModelViewSet):

    queryset = PomodoroTask.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [UserPermission]
    lookup_field = 'user'

    def list(self, request):
        username = request.query_params['username']
        task_state = request.query_params['task_state']
        tasks_by_user_queryset = PomodoroTask.objects.filter(user=1, end_task=task_state).order_by('-pub_date')
        serializer = TaskSerializer(tasks_by_user_queryset, many=True)
        return Response(serializer.data)
