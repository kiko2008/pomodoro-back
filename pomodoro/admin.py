from django.contrib import admin
from .models import PomodoroConf, PomodoroTask


@admin.register(PomodoroConf)
class PomodoroConfAdmin(admin.ModelAdmin):
    list_display = ['id', 'pomodoro_time', 'pomodoro_shortbreak_time', 'pomodoro_longbreak_time']


@admin.register(PomodoroTask)
class PomodoroTaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'pub_date', 'number_pomodoro_used', 'end_task']

