from core.credit.infra.credit_django_app.filters import CreditFilter
from rest_framework.viewsets import ModelViewSet
from .models import Credit, PaymentSaveModel
from .serializers import CreditModelSerializer, PaymentSaveModelSerializer
from rest_framework.views import APIView
from django_project.settings import MICROSSERVICE_URL
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests
import threading
import time
from django.http import JsonResponse
from core.credit.domain.actions.get_payment_status import get_payment_status
from core.cafeteria.infra.cafeteria_django_app.models import TurnstileEntrance
from datetime import datetime
from django.db.models import F
from core.campus.infra.campus_django_app.models import Student


class CreditModelViewSet(ModelViewSet):
    queryset = Credit.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]
    filterset_class = CreditFilter

    def get_serializer_class(self):
        if self.action == "list":
            return CreditModelSerializer
        elif self.action == "retrieve":
            return CreditModelSerializer
        return CreditModelSerializer


class PaymentSaveModelModelViewSet(ModelViewSet):
    queryset = PaymentSaveModel.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action == "list":
            return PaymentSaveModelSerializer
        elif self.action == "retrieve":
            return PaymentSaveModelSerializer
        return PaymentSaveModelSerializer


class PaymentSaveModelPatchAPIView(APIView):
    def patch(self, request, payment_id, format=None):
        try:
            payment = PaymentSaveModel.objects.get(
                id=payment_id
            )  # Ensure payment_id ends with a slash
            payment.status = request.data.get("status")
            payment.date_approved = True
            payment.time_approved = datetime.now()
            payment.student = Student.objects.filter(
                user__id=request.data.get("student")
            ).first()
            payment.save()

            print(payment.student)
            print(payment.transaction_amount)

            credit, created = Credit.objects.get_or_create(student=payment.student)
            credit.credit_value += 30
            print(credit.credit_value)
            print(credit.credit_value + 30)
            credit.save()
            # Save the updated payment details
            return Response(status=status.HTTP_200_OK)  # Return success response
        except PaymentSaveModel.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND, data={"error": "Payment not found"}
            )


class PaymentAPIView(APIView):
    PAYMENT_URL = f"{MICROSSERVICE_URL}/pay/"

    def post(self, request) -> None:
        payload = request.data

        try:
            response = requests.post(
                self.PAYMENT_URL,
                json=payload,
                timeout=10,
            )

            if response.status_code in [200, 201]:
                payment_data = response.json()

                def parse_date(date_str):
                    if date_str:
                        try:
                            # Parse o ISO 8601 e retorne no formato YYYY-MM-DD
                            return datetime.fromisoformat(date_str).date()
                        except ValueError:
                            pass  # Deixe como None se a conversão falhar
                    return None

                payment_data_mapped = {
                    "id": payment_data.get("id"),
                    "status": payment_data.get("status"),
                    "status_detail": payment_data.get("status_detail"),
                    "transaction_amount": payment_data.get("transaction_amount"),
                    "payment_method": payment_data.get("payment_method"),
                    "date_created": parse_date(payment_data.get("date_created")),
                    "qr_code": payment_data.get("qrCode"),
                    "qr_code_base64": payment_data.get("qrCodeBase64"),
                    "date_approved": parse_date(payment_data.get("date_approved")),
                }

                PaymentSaveModel.objects.create(**payment_data_mapped)
                # time.sleep(5)
                # thread = threading.Thread(target=get_payment_status, args=(payment_data.get('uuid'), None))
                # thread.start()
                return Response(payment_data, status=response.status_code)
        except Exception as e:
            print(e)
            return Response(str(2), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PaymentDetailAPIView(APIView):
    PAYMENT_DETAIL_URL = (
        f"{MICROSSERVICE_URL}/pay/{{}}/"  # Ensure URL ends with a slash
    )

    def get(self, request, payment_id, format=None):
        try:
            response = requests.get(
                self.PAYMENT_DETAIL_URL.format(payment_id),
                timeout=10,
            )

            if response.status_code == 200:
                payment_data = response.json()
                return Response(payment_data, status=response.status_code)
            else:
                return Response(
                    response.json(),
                    status=response.status_code,
                )
        except requests.RequestException as e:
            return Response(
                {"error": "Error connecting to microservice", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


@api_view(["GET"])
def get_payment_relatory(request):
    user_id = request.query_params.get("user_id")
    print(user_id)

    student_id = Student.objects.filter(user__id=user_id).first().id

    if not student_id:
        return Response({"error": "Estudante não encontrado."}, status=400)

    payments = PaymentSaveModel.objects.filter(student__id=student_id).values(
        "id", "transaction_amount", "date_created"
    )

    entrances = TurnstileEntrance.objects.filter(student__id=student_id).values(
        "id", "date"
    )

    for payment in payments:
        payment["type"] = "entrada"
        payment["value"] = payment.pop(
            "transaction_amount", None
        )  # Renomeia transaction_amount para value
        payment["date"] = payment.pop("date_created")  # Padroniza o campo de data

    entrances = TurnstileEntrance.objects.filter(student__id=student_id).values(
        "id", "date"
    )

    for entrance in entrances:
        entrance["type"] = "saida"
        entrance["value"] = 11.0  # Valor fixo

    # Combinar as transações e ordená-las pela data
    transactions = list(payments) + list(entrances)

    transactions = [t for t in transactions if t["date"] is not None]

    transactions.sort(key=lambda x: x["date"])

    return Response(transactions)
