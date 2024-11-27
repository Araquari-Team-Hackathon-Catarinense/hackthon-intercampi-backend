from django_filters.rest_framework import CharFilter

from core.__seedwork__.infra.django_app.basefilter import BaseFilter
from core.cafeteria.infra.cafeteria_django_app.models import DietaryRestrictions,Menu,TurnstileEntrance

class DietaryRestrictionsFilter(BaseFilter):
    search = CharFilter(
        field_name="search", method="global_search_for_strings_and_numbers"
    )

    class Meta:
        model = DietaryRestrictions
        fields = ["search"]

class MenuFilter(BaseFilter):
    search = CharFilter(
        field_name="search", method="global_search_for_strings_and_numbers"
    )
    date = CharFilter(
        field_name="date", lookup_expr="exact"
    )

    class Meta:
        model = Menu
        fields = ["search", "date"]

class TurnstileEntranceFilter(BaseFilter):
    search = CharFilter(
        field_name="search", method="global_search_for_strings_and_numbers"
    )

    class Meta:
        model = TurnstileEntrance
        fields = ["search"]
