from rest_framework.routers import DefaultRouter

from core.campus.infra.campus_django_app.router import router as campus_router

from core.uploader.infra.uploader_django_app.router import router as uploader_router
from core.user.infra.user_django_app.router import router as user_router
from core.class_name.infra.class_django_app.router import router as class_router
from core.cafeteria.infra.cafeteria_django_app.router import router as cafeteria_router
from core.credit.infra.credit_django_app.router import router as credit_router


router = DefaultRouter()
router.registry.extend(campus_router.registry)
router.registry.extend(class_router.registry)
router.registry.extend(uploader_router.registry)
router.registry.extend(user_router.registry)
router.registry.extend(cafeteria_router.registry)
router.registry.extend(credit_router.registry)
