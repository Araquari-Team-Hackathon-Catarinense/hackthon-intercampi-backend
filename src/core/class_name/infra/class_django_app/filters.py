from django_filters.rest_framework import CharFilter, BooleanFilter

from core.__seedwork__.infra.django_app.basefilter import BaseFilter
from core.class_name.infra.class_django_app.models import ClassName

class ClassNameFilter(BaseFilter):
    name = CharFilter(field_name="name", method="global_filter_for_strings")
    free_lunch = BooleanFilter(field_name="free_lunch")

    class Meta:
        model = ClassName
        fields = ["name", "free_lunch"]