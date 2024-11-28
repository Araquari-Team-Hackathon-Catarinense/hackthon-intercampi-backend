from typing import final
from django.shortcuts import render
import datetime
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import DietaryRestrictions, Menu, TurnstileEntrance
from core.campus.infra.campus_django_app.models import Student
from core.credit.infra.credit_django_app.models import Credit
from core.cafeteria.infra.cafeteria_django_app.models import Cafeteria
from .serializers import (
    DietaryRestrictionsSerializer,
    MenuSerializer,
    TurnstileEntranceSerializer,
    TurnstileEntranceCreateSerializer,
    MenuCreateSerializer,
)
from core.cafeteria.infra.cafeteria_django_app.filters import (
    DietaryRestrictionsFilter,
    MenuFilter,
    TurnstileEntranceFilter,
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now, timedelta
from datetime import timedelta
from django_project.pagination import VirtualTruckPagination


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


@api_view(["POST"])
def register_entrance(request):
    try:
        registration = request.data.get("registration")

        if Student.objects.get(registration=registration):
            today = today = datetime.date.today()
            student = Student.objects.get(registration=registration)

            # if TurnstileEntrance.objects.filter(student=student, date=today).exists():
            #     return Response(
            #         {"message": "Entrada já registrada"},
            #         status=status.HTTP_400_BAD_REQUEST,
            #     )

            classes = student.class_name

            day_of_week = str((today.weekday() + 1) % 7)

            print(day_of_week)
            print(classes.free_afternoons)

            if day_of_week in classes.free_afternoons:
                TurnstileEntrance.objects.create(
                    student=student, entry_time=now(), date=today, payment=False
                )
                return Response(
                    {"message": "Entrada gratuita"},
                    status=status.HTTP_200_OK,
                )
            else:
                credit = Credit.objects.get(student=student)
                cafeteria = Cafeteria.objects.get(campus=student.class_name.campus)

                if credit.credit_value >= cafeteria.lunch_price:
                    TurnstileEntrance.objects.create(
                        student=student, entry_time=now(), date=today, payment=True
                    )
                    credit.credit_value -= cafeteria.lunch_price
                    credit.save()
                    return Response(
                        {"message": "Entrada paga"},
                        status=status.HTTP_200_OK,
                    )
                else:
                    return Response(
                        {"message": "Creditos insuficientes"},
                        status=status.HTTP_403_FORBIDDEN,
                    )

        else:
            return Response(
                {"message": "Matrícula não encontrada"},
                status=status.HTTP_404_NOT_FOUND,
            )

    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_active_entrances(request):
    try:
        today = datetime.date.today()
        entrances = TurnstileEntrance.objects.filter(
            date=today,
            entry_time__lte=now(),
            entry_time__gte=now() - timedelta(minutes=2),
        )

        paginator = VirtualTruckPagination()
        paginated_entrances = paginator.paginate_queryset(entrances, request)

        if not entrances.exists():
            return paginator.get_paginated_response([])

        serializer = TurnstileEntranceSerializer(paginated_entrances, many=True)
        return paginator.get_paginated_response(serializer.data)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_month_entrances(request):
    try:
        today = datetime.date.today()
        entrances = TurnstileEntrance.objects.filter(
            date__month=today.month,
            date__year=today.year,
        )
        last_month_entrances = TurnstileEntrance.objects.filter(
            date__month=today.month - 1,
            date__year=today.year,
        )

        data = {
            "current_month_entrances": TurnstileEntranceSerializer(entrances, many=True).data,
            "last_month_entrances": TurnstileEntranceSerializer(last_month_entrances, many=True).data,
        }
        return Response(data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
