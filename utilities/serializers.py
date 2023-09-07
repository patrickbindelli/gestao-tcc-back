from rest_framework import serializers
from .models import UsefulFile, UsefulLink


class UsefulFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulFile
        fields = [
            "id",
            "title",
            "file",
        ]


class UsefulLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulLink
        fields = [
            "id",
            "title",
            "url",
        ]
