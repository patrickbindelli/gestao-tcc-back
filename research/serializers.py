from rest_framework import serializers
from .models import Invite, ThesisProject
from users.models import Student


class InviteSerializer(serializers.ModelSerializer):
    sender_name = serializers.StringRelatedField(source="sender", read_only=True)
    receiver_name = serializers.StringRelatedField(source="receiver", read_only=True)

    subject = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    def get_subject(self, obj):
        return dict(ThesisProject.RESEARCH_CHOICES).get(obj.type)

    def get_status(self, obj):
        return "Aceito" if obj.accepted else "Pendente"

    class Meta:
        model = Invite
        fields = [
            "id",
            "subject",
            "sender_name",
            "receiver_name",
            "created_at",
            "limit_date",
            "status",
        ]


class ThesisProjectSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    responsible = serializers.SerializerMethodField()
    advisor_name = serializers.StringRelatedField(source="advisor", read_only=True)
    subject = serializers.SerializerMethodField()

    def get_subject(self, obj):
        return dict(ThesisProject.RESEARCH_CHOICES).get(obj.type)

    def get_author(self, obj):
        author = obj.author
        if author:
            return {
                "id": author.id,
                "name": f"{author.user}" if author.user else "",
            }
        return None

    def get_responsible(self, obj):
        responsible = obj.responsible
        if responsible:
            return {
                "id": responsible.id,
                "name": f"{responsible.user}" if responsible.user else "",
            }
        return None

    class Meta:
        model = ThesisProject
        fields = [
            "id",
            "title",
            "description",
            "subject",
            "author",
            "advisor_name",
            "approved",
            "approved_at",
            "committee",
            "defense_date",
            "invite",
            "responsible",
            "file",
        ]
