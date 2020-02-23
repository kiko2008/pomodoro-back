from django.contrib.auth.models import User
from pomodoro.models import PomodoroTask
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ('id')


class TaskSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    description = serializers.CharField()
    pub_date = serializers.DateTimeField()
    number_pomodoro_used = serializers.IntegerField()
    end_task = serializers.BooleanField()
    user = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all())

    def create(self, request_data):
        pomodoro_task = PomodoroTask()
        return self.update(pomodoro_task, request_data)

    def update(self, instance, request_data):
        if request_data.get('description') is not None:
            instance.description = request_data.get('description')

        if request_data.get('pub_date') is not None:
            instance.pub_date = request_data.get('pub_date')

        if request_data.get('number_pomodoro_used') is not None:
            instance.number_pomodoro_used = request_data.get('number_pomodoro_used')

        if request_data.get('end_task') is not None:
            instance.end_task = request_data.get('end_task')

        if request_data.get('user') is not None:
            instance.user = request_data.get('user')

        instance.save()
        return instance
