
from rest_framework import serializers

from core.uploader.infra.uploader_django_app.models import Document
from core.uploader.infra.uploader_django_app.serializers import DocumentSerializer

from .models import Campus, Employee, Student
from core.user.infra.user_django_app.serializers import UserDetailSerializer


class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = [
            "id",
            "name",
            "email"
        ]

class EmployeeSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
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
    user = UserDetailSerializer()
    campus = CampusSerializer()
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
