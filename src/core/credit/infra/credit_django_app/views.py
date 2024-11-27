
from core.credit.infra.credit_django_app.filters import CreditFilter
from rest_framework.viewsets import ModelViewSet
from .models import Credit, PaymentSaveModel
from .serializers import CreditModelSerializer, PaymentSaveModelSerializer
from rest_framework.views import APIView
from django_project.settings import MICROSSERVICE_URL
from rest_framework.response import Response
from rest_framework import status
import requests
import threading
import time
from django.http import JsonResponse
from core.credit.domain.actions.get_payment_status import get_payment_status
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
                print(response.json())
                
                payment_data_mapped = {
                    'status': payment_data.get('status'),
                    'status_detail': payment_data.get('status_detail'),
                    'transaction_amount': payment_data.get('transaction_amount'),
                    'payment_method': payment_data.get('payment_method'),
                    'date_created': payment_data.get('date_created'),
                    'qr_code': payment_data.get('qrCode'),
                    'qr_code_base64': payment_data.get('qrCodeBase64'),
                    'date_approved': payment_data.get('date_approved')
                }

               

                PaymentSaveModel.objects.create(**payment_data_mapped)

                threading.Timer(5, get_payment_status(self, args=[payment_data['id']])).start()
                return Response(payment_data, status=response.status_code)
        except requests.RequestException as e:
            return Response(
                {"error": "Error connecting to microservice", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        
       
