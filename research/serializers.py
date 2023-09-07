from rest_framework import serializers
from .models import Invite, ThesisProject


class InviteSerializer(serializers.ModelSerializer):
    sender_name = serializers.StringRelatedField(source="sender", read_only=True)
    receiver_name = serializers.StringRelatedField(source="receiver", read_only=True)

    class Meta:
        model = Invite
        fields = [
            "id",
            "type",
            "sender",
            "sender_name",
            "receiver",
            "receiver_name",
            "created_at",
            "accepted",
        ]


class ThesisProjectSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()

    class Meta:
        model = ThesisProject
        fields = [
            "id",
            "title",
            "description",
            "authors",
            "advisor",
            "approved",
            "approved_at",
            "committee",
            "defense_date",
            "invite",
        ]

    def get_authors(self, obj):
        authors = obj.authors.all()
        author_data = [{"id": author.id, "name": author.username} for author in authors]
        return author_data
