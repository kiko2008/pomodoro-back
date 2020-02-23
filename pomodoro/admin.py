from django.contrib import admin
from .models import PomodoroTask


@admin.register(PomodoroTask)
class PomodoroTaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'pub_date', 'number_pomodoro_used', 'end_task']
