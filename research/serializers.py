from rest_framework import serializers
from .models import Invite, ThesisProject
from users.models import Student


class InviteSerializer(serializers.ModelSerializer):
    advised = serializers.SerializerMethodField()
    advisor = serializers.SerializerMethodField()

    def get_advised(self, obj):
        advised = obj.advised
        if advised:
            return {
                "id": advised.id,
                "name": f"{advised.user}" if advised.user else "",
            }
        return None

    def get_advisor(self, obj):
        advisor = obj.advisor
        if advisor:
            return {
                "id": advisor.id,
                "name": f"{advisor.user}" if advisor.user else "",
            }
        return None

    type = serializers.SerializerMethodField()

    def get_type(self, obj):
        return dict(ThesisProject.RESEARCH_CHOICES).get(obj.type)

    class Meta:
        model = Invite
        fields = [
            "id",
            "type",
            "advisor",
            "advised",
            "created_at",
            "limit_date",
            "accepted",
        ]


class ThesisProjectSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    advisor = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    file_name = serializers.SerializerMethodField()
    file_size = serializers.SerializerMethodField()

    def get_file_name(self, obj):
        if obj.file:
            return obj.file.name
        return None

    def get_file_size(self, obj):
        if obj.file:
            return obj.file.size
        return None

    def get_type(self, obj):
        return dict(ThesisProject.RESEARCH_CHOICES).get(obj.type)

    def get_author(self, obj):
        author = obj.author
        if author:
            return {
                "id": author.id,
                "name": f"{author.user}" if author.user else "",
            }
        return None

    def get_advisor(self, obj):
        advisor = obj.advisor
        if advisor:
            return {
                "id": advisor.id,
                "name": f"{advisor.user}" if advisor.user else "",
            }
        return None

    class Meta:
        model = ThesisProject
        fields = [
            "id",
            "title",
            "description",
            "type",
            "author",
            "advisor",
            "approved",
            "approved_at",
            "committee",
            "defense_date",
            "invite",
            "file",
            "file_name",
            "file_size",
        ]
