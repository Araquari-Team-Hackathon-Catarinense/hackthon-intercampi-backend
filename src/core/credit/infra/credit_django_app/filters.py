from django_filters.rest_framework import CharFilter

from core.__seedwork__.infra.django_app.basefilter import BaseFilter
from core.credit.infra.credit_django_app.models import Credit

class CreditFilter(BaseFilter):
    search = CharFilter(
        field_name="search", method="global_search_for_strings_and_numbers"
    )

    class Meta:
        model = Credit
        fields = ["search"]