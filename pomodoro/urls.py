from django.urls import path, include
from rest_framework.routers import DefaultRouter

from pomodoro.api import PomodoroConfViewSet, PomodoroTaskViewSet

router = DefaultRouter()
router.register('conf', PomodoroConfViewSet, base_name='conf')
router.register('tasks', PomodoroTaskViewSet, base_name='tasks')


urlpatterns = [
    # API REST
    path('api/1.0/', include(router.urls)),
]
