from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .models import ClassName
from .serializers import ClassNameSerializer

class ClassNameModelViewSet(ModelViewSet):
    queryset = ClassName.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    # def get_queryset(self):
    #     company_id = getattr(self.request, "campus_id", None)

    #     if company_id:
    #         return Employee.objects.filter(company__id=company_id)
    #     raise CompanyNotInHeader

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ClassNameSerializer
        return ClassNameSerializer