from .views import ClassNameModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"class/classes", ClassNameModelViewSet, basename="campus-class")
