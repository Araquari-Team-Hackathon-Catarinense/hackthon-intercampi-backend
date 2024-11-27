from rest_framework import serializers

from .models import DietaryRestrictions, Menu, TurnstileEntrance

class MenuSerializer(serializers.ModelSerializer):
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


class DietaryRestrictionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietaryRestrictions
        fields = [
            "id",
            "description"
        ]
        read_only_fields = ["id"]

class TurnstileEntranceSerializer(serializers.ModelSerializer):
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