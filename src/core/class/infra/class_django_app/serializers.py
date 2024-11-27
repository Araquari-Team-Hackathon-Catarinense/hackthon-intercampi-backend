
from rest_framework import serializers

from core.uploader.infra.uploader_django_app.models import Document
from core.uploader.infra.uploader_django_app.serializers import DocumentSerializer
from django_project.settings import BASE_URL

from .models import ClassName



class ClassNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields = [
            "id",
            "name",
            "free_afternoons",
            "free_lunch"
        ]
        read_only_fields = ["id"]
        extra_kwargs = {"campus": {"write_only": True}}