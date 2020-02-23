from rest_framework.permissions import BasePermission


class PomodoroPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser or view.action in ['create', 'retrieve', 'update', 'destroy', 'partial_update', 'list']

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.data['userid'] == obj.user.id
