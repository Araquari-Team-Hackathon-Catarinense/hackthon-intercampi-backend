from django_filters.rest_framework import CharFilter,DateFilter

from core.__seedwork__.infra.django_app.basefilter import BaseFilter
from core.credit.infra.credit_django_app.models import Credit

class CreditFilter(BaseFilter):
    search = CharFilter(
        field_name="search", method="global_search_for_strings_and_numbers"
    )
    credit_value= CharFilter(
        field_name="credit_value", method="global_filter_for_strings"
    )


    class Meta:
        model = Credit
        fields = ["search", "credit_value"]