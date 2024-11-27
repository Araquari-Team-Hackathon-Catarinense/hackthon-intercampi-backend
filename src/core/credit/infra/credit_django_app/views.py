
from rest_framework.viewsets import ModelViewSet
from .models import Credit
from .serializers import CreditModelSerializer


class CreditModelViewSet(ModelViewSet):
    queryset = Credit.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]
    # filterset_class = CompanyFilter

    def get_serializer_class(self):
        if self.action == "list":
            return CreditModelSerializer
        elif self.action == "retrieve":
            return CreditModelSerializer
        return CreditModelSerializer