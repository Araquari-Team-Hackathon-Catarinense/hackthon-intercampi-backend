from rest_framework.routers import DefaultRouter
from .views import DietaryRestrictionsViewSet,MenuViewSet,TurnstileEntranceViewSet, TurnstileEntranceBeforeMinutesViewSet

router = DefaultRouter()

router.register(r"cafeteria/dietary-restrictions", DietaryRestrictionsViewSet, basename="cafeteria-dietary-restrictions")
router.register(r"cafeteria/menus",MenuViewSet, basename ="cafeteria-menu")
router.register(r"cafeteria/turnstile-entrances", TurnstileEntranceViewSet, basename="cafeteria-turnstile-entrance")
router.register(r"cafeteria/turnstile-entrances-before-minutes", TurnstileEntranceBeforeMinutesViewSet, basename="cafeteria-turnstile-entrance-before-minutes")