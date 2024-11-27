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
)
from core.uploader.infra.uploader_django_app.models import Document
from core.uploader.infra.uploader_django_app.serializers import DocumentUploadSerializer

from .models import Campus, Employee, Student, ClassName


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
