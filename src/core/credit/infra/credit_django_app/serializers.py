from .models import Credit
from rest_framework.serializers import ModelSerializer

class CreditModelSerializer(ModelSerializer):
    class Meta:
        model = Credit
        fields = [
            "id",
            "credit_value",
            "date"
        ]
        read_only_fields = ["id"]

