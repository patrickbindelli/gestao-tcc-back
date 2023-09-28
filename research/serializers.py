from rest_framework import serializers
from .models import Invite, ThesisProject


class InviteSerializer(serializers.ModelSerializer):
    sender_name = serializers.StringRelatedField(source="sender", read_only=True)
    receiver_name = serializers.StringRelatedField(source="receiver", read_only=True)

    subject = serializers.SerializerMethodField()

    def get_subject(self, obj):
        return dict(ThesisProject.RESEARCH_CHOICES).get(obj.type)

    class Meta:
        model = Invite
        fields = [
            "id",
            "subject",
            "sender_name",
            "receiver_name",
            "created_at",
            "accepted",
        ]


class ThesisProjectSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()

    def get_authors(self, obj):
        authors = obj.authors.all()
        author_data = [
            {"id": author.id, "name": f"{author.first_name} {author.last_name}"}
            for author in authors
        ]
        return author_data

    advisor_name = serializers.StringRelatedField(source="advisor", read_only=True)

    subject = serializers.SerializerMethodField()

    def get_subject(self, obj):
        return dict(ThesisProject.RESEARCH_CHOICES).get(obj.type)

    class Meta:
        model = ThesisProject
        fields = [
            "id",
            "title",
            "description",
            "subject",
            "authors",
            "advisor_name",
            "approved",
            "approved_at",
            "committee",
            "defense_date",
            "invite",
        ]
