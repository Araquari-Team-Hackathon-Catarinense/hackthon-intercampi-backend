from core.campus.infra.campus_django_app.filters import (
    CampusFilter,
    EmployeeFilter,
    StudentFilter,
    ClassNameFilter,
)
from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from core.__seedwork__.domain.exceptions import CompanyNotInHeader
from core.campus.infra.campus_django_app.serializers import (
    EmployeeSerializer,
    StudentSerializer,
    CampusSerializer,
    EmployeeCreateSerializer,
    StudentCreateSerializer,
    ClassNameSerializer,
    ChatSerializer
)
from core.uploader.infra.uploader_django_app.models import Document
from core.uploader.infra.uploader_django_app.serializers import DocumentUploadSerializer

from .models import Campus, Employee, Student, ClassName, Chat

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from django_project.settings import MICROSSERVICE_URL


@extend_schema(tags=["Core"])
class CampusViewSet(ModelViewSet):
    queryset = Campus.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]
    filterset_class = CampusFilter

    def get_serializer_class(self):
        if self.action == "list":
            return CampusSerializer
        elif self.action == "retrieve":
            return CampusSerializer
        return CampusSerializer


@extend_schema(tags=["Company"])
class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]
    filterset_class = EmployeeFilter

    def get_queryset(self):
        campus_id = getattr(self.request, "campus_id", None)

        if campus_id:
            return Employee.objects.filter(campus__id=campus_id)
        raise CompanyNotInHeader

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return EmployeeSerializer
        return EmployeeCreateSerializer


@extend_schema(tags=["Company"])
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]
    filterset_class = StudentFilter

    def get_queryset(self):
        campus_id = getattr(self.request, "campus_id", None)

        if campus_id:
            return Student.objects.filter(class_name__campus__id=campus_id)
        raise CompanyNotInHeader

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return StudentSerializer
        return StudentCreateSerializer


class ClassNameModelViewSet(ModelViewSet):
    queryset = ClassName.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]
    filterset_class = ClassNameFilter

    def get_queryset(self):
        campus_id = getattr(self.request, "campus_id", None)

        print
        if campus_id:
            return ClassName.objects.filter(campus__id=campus_id)
        else:
            return ClassName.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ClassNameSerializer
        return ClassNameSerializer


class ChatModelViewSet(ModelViewSet):
    queryset = Chat.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        return ChatSerializer
    
class ChatGPTGetAPIView(APIView):
    CHATGPT_URL = f"{MICROSSERVICE_URL}chat/chatgpt/"
    def get (self, request):
        try:
            response = requests.get(
                self.CHATGPT_URL.format(),
                timeout=10,
            )
            if response.status_code == 200:
                chat_data = response.json()
                return Response(chat_data, status=response.status_code)
            else:
                return Response(
                    response.json(),
                    status=response.status_code,
                )
        except requests.RequestException as e:
            return Response(
                {"error": "Error connecting to microservice", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
