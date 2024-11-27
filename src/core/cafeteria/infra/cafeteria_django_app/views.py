
from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import DietaryRestrictions, Menu, TurnstileEntrance
from .serializers import DietaryRestrictionsSerializer, MenuSerializer,  TurnstileEntranceSerializer
from core.cafeteria.infra.cafeteria_django_app.filters import DietaryRestrictionsFilter, MenuFilter, TurnstileEntranceFilter


class DietaryRestrictionsViewSet(ModelViewSet):
    queryset = DietaryRestrictions.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]
    filterset_class = DietaryRestrictionsFilter

    def get_serializer_class(self):
        if self.action == "list":
            return DietaryRestrictionsSerializer
        elif self.action == "retrieve":
            return DietaryRestrictionsSerializer
        return DietaryRestrictionsSerializer
    

class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]
    filterset_class = MenuFilter

    def get_serializer_class(self):
        if self.action == "list":
            return MenuSerializer
        elif self.action == "retrieve":
            return MenuSerializer
        return MenuSerializer

class TurnstileEntranceViewSet(ModelViewSet):
    queryset = TurnstileEntrance.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]
    filterset_class = TurnstileEntranceFilter

    def get_serializer_class(self):
        if self.action == "list":
            return TurnstileEntranceSerializer
        elif self.action == "retrieve":
            return TurnstileEntranceSerializer
        return TurnstileEntranceSerializer