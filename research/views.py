from .models import ThesisProject, Invite
from .serializers import ThesisProjectSerializer, InviteSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser


class ThesisProjectsViewSet(viewsets.ModelViewSet):
    queryset = ThesisProject.objects.all()
    serializer_class = ThesisProjectSerializer

    @action(detail=False, methods=["get"])
    def ongoing(self, request):
        user = request.user
        queryset = self.get_queryset().filter(approved=False, author__user=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def approved(self, request):
        user = request.user
        queryset = self.get_queryset().filter(approved=True, author__user=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class InvitesViewSet(viewsets.ModelViewSet):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        queryset = queryset.filter(receiver__user=user)
        return queryset
