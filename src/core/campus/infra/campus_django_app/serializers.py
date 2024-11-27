
from rest_framework import serializers

from core.uploader.infra.uploader_django_app.models import Document
from core.uploader.infra.uploader_django_app.serializers import DocumentSerializer

from .models import Campus, Employee, Student


class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = [
            "id",
            "name",
            "email"
        ]

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id",
            "campus",
            "user",
            "siape"
        ]
        read_only_fields = ["id"]
        extra_kwargs = {"campus": {"write_only": True}}


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "id",
            "user",
            "campus",
            "registration",
        ]
        read_only_fields = ["id"]
        extra_kwargs = {"campus": {"write_only": True}}
