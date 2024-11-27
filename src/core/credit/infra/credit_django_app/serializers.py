from .models import Credit, PaymentSaveModel
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


class PaymentSaveModelSerializer(ModelSerializer):
    class Meta:
        model = PaymentSaveModel
        fields = [
            "id",
            "status",
            "status_detail",
            "transaction_amount",
            "payment_method",
            "date_created",
            "qr_code",
            "qr_code_base64",
            "date_approved"
        ]
        read_only_fields = ["id"]