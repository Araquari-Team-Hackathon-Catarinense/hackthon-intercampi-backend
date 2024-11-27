from django.forms import model_to_dict
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.uploader.infra.uploader_django_app.serializers import DocumentUploadSerializer
from core.user.infra.user_django_app.filters import UserFilter

from .models import User
from core.campus.infra.campus_django_app.models import Student
from core.campus.infra.campus_django_app.serializers import StudentCreateSerializer
from .serializers import (
    UserCreateSerializer,
    UserDetailSerializer,
    UserListSerializer,
)


@extend_schema(tags=["User"])
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]
    authentication_classes = []
    filterset_class = UserFilter

    def get_serializer_class(self):
        if self.action == "list":
            return UserListSerializer
        elif self.action == "retrieve":
            return UserDetailSerializer
        return UserCreateSerializer

    @action(
        detail=True,
        methods=["post"],
        url_path="upload-avatar",
    )
    def upload_avatar(self, request, pk=None, *args, **kwargs):
        try:
            user: User = self.get_object()
            data = request.data.copy()
            if (
                "description" not in data
                or data["description"] is None
                or data["description"] == ""
            ):
                data["description"] = f"Avatar do usuario {user.name}"
            data["file"] = request.FILES.get("file")
            serializer = DocumentUploadSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            if user.avatar:
                user.avatar.delete()
            user.avatar = serializer.instance
            user.save()
            user_detail_serializer = UserDetailSerializer(user)
            return Response(user_detail_serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=["User"])
@api_view(["POST"])
def register(request):
    try:
        error = list()
        user_data = {
            "name": request.data.get("name"),
            "email": request.data.get("email"),
            "cpf": request.data.get("cpf"),
            "password": request.data.get("password")
        }

        if User.objects.filter(email=user_data["email"]).exists():
            error.append({
                "email": "Email já cadastrado"
            })

        if User.objects.filter(cpf=user_data["cpf"]).exists():
            error.append(
                {
                    "cpf": "CPF já cadastrado"
                }
            )

        if Student.objects.filter(registration=request.data.get("registration")).exists():
            error.append(
                {
                    "registration": "Matrícula já cadastrada"
                }
            )

        print(len(error))
        if len(error) > 0:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

        user_serializer = UserCreateSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        if user_serializer.instance is not None:
            print(request.data.get("campus"))
            student_data = {
                "campus": request.data.get("campus"),
                "registration": request.data.get("registration"),
                "user": str(user_serializer.instance.id)
            }
            student_serializer = StudentCreateSerializer(data=student_data)
            student_serializer.is_valid(raise_exception=True)
            student_serializer.save()
            return Response(student_serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        if User.objects.filter(email=user_data["email"]).exists():
            User.objects.filter(email=user_data["email"]).delete()
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)    
