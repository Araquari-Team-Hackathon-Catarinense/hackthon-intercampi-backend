from rest_framework.routers import DefaultRouter
from .views import DietaryRestrictionsViewSet,MenuViewSet

router = DefaultRouter()

router.register(r"cafeteria/dietary-restrictions", DietaryRestrictionsViewSet, basename="cafeteria-dietary-restrictions")
router.register(r"cafeteria/menu",MenuViewSet, basename ="cafeteria-menu")