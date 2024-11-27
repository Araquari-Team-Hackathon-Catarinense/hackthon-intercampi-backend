import requests
from django.core.exceptions import ObjectDoesNotExist
from core.credit.infra.credit_django_app.models import PaymentSaveModel
from django_project.settings import MICROSSERVICE_URL

def get_payment_status(payment_id, args):
    try:
        response = requests.get(f"{MICROSSERVICE_URL}/pay/{payment_id}", timeout=10)

        if response.status_code == 200:
            payment_status = response.json()
            print(payment_status)
            try:
                payment = PaymentSaveModel.objects.get(id=payment_id)
                payment.status = payment_status.get('status')
                payment.status_detail = payment_status.get('status_detail')
                payment.transaction_amount = payment_status.get('transaction_amount')
                payment.payment_method = payment_status.get('payment_method')
                payment.date_created = payment_status.get('date_created')
                payment.qr_code = payment_status.get('qrCode')
                payment.qr_code_base64 = payment_status.get('qrCodeBase64')
                payment.date_approved = payment_status.get('date_approved')
                payment.save()
            except ObjectDoesNotExist:
                print(f"Payment with id {payment_id} does not exist.")
        else:
            print(f"Error in microservice: {response.json()}")
    except requests.RequestException as e:
        print(f"Error connecting to microservice: {str(e)}")