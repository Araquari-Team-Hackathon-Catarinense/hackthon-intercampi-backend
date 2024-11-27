from rest_framework.routers import DefaultRouter

from core.campus.infra.campus_django_app.views import (
    CampusViewSet,
    StudentViewSet,
    EmployeeViewSet,
)

router = DefaultRouter()

router.register(r"campus/campi", CampusViewSet, basename="campus-campus")
router.register(r"campus/students", StudentViewSet, basename="campus-student")
router.register(r"campus/employees", EmployeeViewSet, basename="campus-employee")
