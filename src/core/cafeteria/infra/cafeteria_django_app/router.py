from rest_framework.routers import DefaultRouter
from .views import DietaryRestrictionsViewSet,MenuViewSet,TurnstileEntranceViewSet

router = DefaultRouter()

router.register(r"cafeteria/dietary-restrictions", DietaryRestrictionsViewSet, basename="cafeteria-dietary-restrictions")
router.register(r"cafeteria/menu",MenuViewSet, basename ="cafeteria-menu")
router.register(r"cafeteria/turnstile-entrance", TurnstileEntranceViewSet, basename="cafeteria-turnstile-entrance")