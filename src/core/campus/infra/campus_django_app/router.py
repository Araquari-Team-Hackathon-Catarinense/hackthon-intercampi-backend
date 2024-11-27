from rest_framework.routers import DefaultRouter

from core.campus.infra.campus_django_app.views import (
    CampusViewSet,
    StudentViewSet,
    EmployeeViewSet,
    ClassNameModelViewSet,
    ChatModelViewSet,
)

router = DefaultRouter()

router.register(r"campus/campuses", CampusViewSet, basename="campus-campus")
router.register(r"campus/students", StudentViewSet, basename="campus-student")
router.register(r"campus/employees", EmployeeViewSet, basename="campus-employee")
router.register(r"class/classes", ClassNameModelViewSet, basename="campus-class")
router.register(r"chat/chats", ChatModelViewSet, basename="campus-chat")

