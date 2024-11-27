
from rest_framework import serializers

from core.uploader.infra.uploader_django_app.models import Document
from core.uploader.infra.uploader_django_app.serializers import DocumentSerializer

from .models import Campus, Employee, ClassName, Student
from core.user.infra.user_django_app.serializers import UserDetailSerializer


from core.user.infra.user_django_app.models import User

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


class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id",
            "campus",
            "user",
            "siape"
        ]
        read_only_fields = ["id"]



class ClassNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields = [
            "id",
            "name",
            "free_afternoons",
            "free_lunch",
            "campus"
        ]
        read_only_fields = ["id"]


class StudentSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    class_name = ClassNameSerializer()
    class Meta:
        model = Student
        fields = [
            "id",
            "user",
            "registration",
            "class_name",
        ]
        read_only_fields = ["id"]


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "id",
            "user",
            "registration",
            "class_name",
        ]
        read_only_fields = ["id"]
