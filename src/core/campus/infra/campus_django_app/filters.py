from django_filters.rest_framework import CharFilter, BooleanFilter, UUIDFilter

from core.__seedwork__.infra.django_app.basefilter import BaseFilter
from core.campus.infra.campus_django_app.models import Campus, Employee, ClassName

# # class CompanyFilter(FilterSet):
# #     search = CharFilter(field_name="search", method="filter_search")

# #     def filter_search(self, queryset, name, value):
# #         try:
# #             return queryset.filter(
# #                 Q(name__icontains=value)
# #                 | Q(trade_name__icontains=value)
# #                 | Q(document_number__icontains=value)
# #             )
# #         except Exception:
# #             return queryset

# #     class Meta:
# #         model = Company
# #         fields = ["search"]


# class CompanyFilter(BaseFilter):
#     search = CharFilter(
#         field_name="search", method="global_search_for_strings_and_numbers"
#     )

#     class Meta:
#         model = Company
#         fields = ["search"]


class CampusFilter(BaseFilter):
    name = CharFilter(field_name="name", method="global_filter_for_strings")
    email = CharFilter(field_name="email", method="global_filter_for_strings")
    search = CharFilter(
        field_name="search", method="global_search_for_strings_and_numbers"
    )

    class Meta:
        model = Campus
        fields = ["name", "email", "search"]


class EmployeeFilter(BaseFilter):
    campus = CharFilter(field_name="campus__name", method="global_filter_for_strings")
    siape = CharFilter(field_name="siape", method="global_filter_for_strings")
    search = CharFilter(
        field_name="search", method="global_search_for_strings_and_numbers"
    )

    class Meta:
        model = Employee
        fields = ["campus", "siape", "search"]


class ClassNameFilter(BaseFilter):
    name = CharFilter(field_name="name", method="global_filter_for_strings")
    free_lunch = BooleanFilter(field_name="free_lunch")
    campus = UUIDFilter(
        field_name="campus__id",
    )

    class Meta:
        model = ClassName
        fields = ["name", "free_lunch"]


class StudentFilter(BaseFilter):
    class_name = CharFilter(
        field_name="student__class_name", method="global_filter_for_strings"
    )
    registration = CharFilter(
        field_name="registration", method="global_filter_for_strings"
    )
    is_cavalo = BooleanFilter(field_name="is_cavalo")
