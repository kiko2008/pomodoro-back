from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.api import UserViewSet
from users.views import LoginView, LogoutView

router = DefaultRouter()
router.register('users', UserViewSet, base_name='users'),

urlpatterns = [
    # API REST
     path('api/1.0/login/', LoginView.as_view(), name='login'),
     path('api/1.0/logout/', LogoutView.as_view(), name='logout'),
     path('api/1.0/', include(router.urls)),
]
