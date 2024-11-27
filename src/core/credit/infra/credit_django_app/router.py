from rest_framework.routers import DefaultRouter
from .views import CreditModelViewSet

router = DefaultRouter()

router.register(r"credit/credit", CreditModelViewSet, basename="credit-credit")
