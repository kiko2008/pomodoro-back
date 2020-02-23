from pomodoro.models import PomodoroTask
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import authentication

from pomodoro.permissions import PomodoroPermission
from pomodoro.serializer import TaskSerializer


class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return


class PomodoroTaskViewSet(ModelViewSet):

    queryset = PomodoroTask.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [PomodoroPermission]

    def list(self, request):
        user_id = request.query_params['userid']
        end_task = request.query_params['end_task']
        tasks_by_user_queryset = PomodoroTask.objects.filter(user=user_id, end_task=end_task).order_by('-pub_date')
        serializer = TaskSerializer(tasks_by_user_queryset, many=True)
        return Response(serializer.data)
