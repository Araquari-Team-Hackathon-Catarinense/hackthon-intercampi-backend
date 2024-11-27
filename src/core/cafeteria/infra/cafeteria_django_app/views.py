
from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import DietaryRestrictions, Menu, TurnstileEntrance
from .serializers import DietaryRestrictionsSerializer, MenuSerializer, TurnstileEntranceSerializer,TurnstileEntranceCreateSerializer, MenuCreateSerializer
from core.cafeteria.infra.cafeteria_django_app.filters import DietaryRestrictionsFilter, MenuFilter, TurnstileEntranceFilter

from django.utils.timezone import now, timedelta
from datetime import timedelta


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
        return MenuCreateSerializer

class TurnstileEntranceViewSet(ModelViewSet):
    queryset = TurnstileEntrance.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]
    filterset_class = TurnstileEntranceFilter

    def get_serializer_class(self):
        if self.action == "list":
            return TurnstileEntranceSerializer
        elif self.action == "retrieve":
            return TurnstileEntranceSerializer
        return TurnstileEntranceCreateSerializer
    

class TurnstileEntranceBeforeMinutesViewSet(ReadOnlyModelViewSet):
    queryset = TurnstileEntrance.objects.all()
    http_method_names = ["get"]

    def get_queryset(self):
      
        current_time = now()
       
        thirty_minutes_ago = current_time - timedelta(minutes=30)

        return TurnstileEntrance.objects.filter(entry_time__gte=thirty_minutes_ago)


    def get_serializer_class(self):
        if self.action == "list":
            return TurnstileEntranceSerializer
        elif self.action == "retrieve":
            return TurnstileEntranceSerializer