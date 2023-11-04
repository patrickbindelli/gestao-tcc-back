from .models import ThesisProject, Invite
from .serializers import ThesisProjectSerializer, InviteSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins


class CustomViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    pass


class ThesisProjectsViewSet(CustomViewSet):
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

    @action(detail=True, methods=["post"])
    def accept(self, request, pk=None):
        user = request.user
        invite = (
            self.get_queryset()
            .filter(accepted=False, id=pk, advised__user=user)
            .first()
        )

        if not invite:
            return Response({"error": "Convite não encontrado."})

        research_title = f"Pesquisa de {invite.advised.user}"

        research = ThesisProject.objects.create(
            invite=invite,
            title=research_title,
            type=invite.type,
            advisor=invite.advisor,
            author=invite.advised,
        )

        research.save()

        invite.accepted = True
        invite.save()

        return Response()

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        queryset = queryset.filter(advised__user=user)
        return queryset
