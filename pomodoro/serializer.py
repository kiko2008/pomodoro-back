from django.contrib.auth.models import User
from pomodoro.models import PomodoroConf, PomodoroTask
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ('id')

class ConfSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    pomodoro_time = serializers.IntegerField()
    pomodoro_shortbreak_time = serializers.IntegerField()
    pomodoro_longbreak_time = serializers.IntegerField()
    user = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all())

    def create(self, request_data):
        pomodoro_conf = PomodoroConf()
        return self.update(pomodoro_conf, request_data)

    def update(self, instance, request_data):
        if request_data.get('pomodoro_time') is not None:
            instance.pomodoro_time = request_data.get('pomodoro_time')

        if request_data.get('pomodoro_shortbreak_time') is not None:
            instance.pomodoro_shortbreak_time = request_data.get('pomodoro_shortbreak_time')

        if request_data.get('pomodoro_longbreak_time') is not None:
            instance.pomodoro_longbreak_time = request_data.get('pomodoro_longbreak_time')

        if request_data.get('user') is not None:
            instance.user = request_data.get('user')

        instance.save()
        return instance


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
