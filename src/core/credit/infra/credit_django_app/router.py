from rest_framework.routers import DefaultRouter
from .views import CreditModelViewSet, PaymentSaveModelModelViewSet

router = DefaultRouter()

router.register(r"credit/credits", CreditModelViewSet, basename="credit-credit")
router.register(r"credit/payment-save-model", PaymentSaveModelModelViewSet, basename="credit-payment-save-model")