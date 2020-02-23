from django.db import models
from django.contrib.auth.models import User


class PomodoroTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')
    number_pomodoro_used = models.IntegerField(blank=True, null=True)
    end_task = models.BooleanField(default=False)
