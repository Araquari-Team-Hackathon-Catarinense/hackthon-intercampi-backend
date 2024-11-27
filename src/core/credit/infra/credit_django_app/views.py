
from core.credit.infra.credit_django_app.filters import CreditFilter
from rest_framework.viewsets import ModelViewSet
from .models import Credit
from .serializers import CreditModelSerializer


class CreditModelViewSet(ModelViewSet):
    queryset = Credit.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]
    filterset_class = CreditFilter

    def get_serializer_class(self):
        if self.action == "list":
            return CreditModelSerializer
        elif self.action == "retrieve":
            return CreditModelSerializer
        return CreditModelSerializer
    

    