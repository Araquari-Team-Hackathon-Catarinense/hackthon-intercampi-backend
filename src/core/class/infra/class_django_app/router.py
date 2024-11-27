from .views import ClassNameModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"class/class", ClassNameModelViewSet, basename="campus-class")