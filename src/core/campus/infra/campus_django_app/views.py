from core.campus.infra.campus_django_app.filters import CampusFilter
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.__seedwork__.domain.exceptions import CompanyNotInHeader
from core.campus.infra.campus_django_app.serializers import (
  EmployeeSerializer,
  StudentSerializer,
  CampusSerializer
)
from core.uploader.infra.uploader_django_app.models import Document
from core.uploader.infra.uploader_django_app.serializers import DocumentUploadSerializer

from .models import Campus, Employee, Student


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

    # def get_queryset(self):
    #     company_id = getattr(self.request, "campus_id", None)

    #     if company_id:
    #         return Employee.objects.filter(__id=company_id)
    #     raise CompanyNotInHeader

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return EmployeeSerializer
        return EmployeeSerializer


@extend_schema(tags=["Company"])
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    # def get_queryset(self):
    #     company_id = getattr(self.request, "campus_id", None)

    #     if company_id:
    #         return Student.objects.filter(company__id=company_id)
    #     raise CompanyNotInHeader

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return StudentSerializer
        return StudentSerializer

