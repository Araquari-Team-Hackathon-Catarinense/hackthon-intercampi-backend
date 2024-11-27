from rest_framework import serializers

from .models import DietaryRestrictions, Menu, TurnstileEntrance
from core.campus.infra.campus_django_app.serializers import StudentSerializer

class DietaryRestrictionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietaryRestrictions
        fields = [
            "id",
            "description"
        ]
        read_only_fields = ["id"]
        
class MenuSerializer(serializers.ModelSerializer):
    dietary_restrictions = DietaryRestrictionsSerializer(many=True)
    class Meta:
        model = Menu
        fields = [
            "id",
            "garnish",
            "main_course",
            "dessert",
            "juice",
            "dietary_restrictions"
        ]
        read_only_fields = ["id"]

class CreateMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class MenuCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = [
            "id",
            "garnish",
            "main_course",
            "dessert",
            "juice",
            "dietary_restrictions"
        ]
        read_only_fields = ["id"]



class TurnstileEntranceSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = TurnstileEntrance
        fields = [
            "id",
            "student",
            "entry_time",
            "date",
            "payment"
        ]
        read_only_fields = ["id"]

class TurnstileEntranceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurnstileEntrance
        fields = [
            "id",
            "student",
            "entry_time",
            "date",
            "payment"
        ]
        read_only_fields = ["id"]
