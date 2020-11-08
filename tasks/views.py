from django_fsm import TransitionNotAllowed
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all()

    @action(detail=True)
    def publish(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk)
        try:
            task.publish()
            task.save()
        except TransitionNotAllowed as e:
            raise ValidationError(e)
        return Response({'status': 'published'})

    @action(detail=True)
    def retract(self, request, pk=None):
        note = get_object_or_404(Task, pk=pk)
        try:
            note.retract()
            note.save()
        except TransitionNotAllowed as e:
            raise ValidationError(e)
        return Response({'status': 'draft'})
