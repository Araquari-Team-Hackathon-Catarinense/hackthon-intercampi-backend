from django_filters.rest_framework import CharFilter

from core.__seedwork__.infra.django_app.basefilter import BaseFilter
from core.campus.infra.campus_django_app.models import Campus

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
    name = CharFilter(field_name="campus_name", method="global_filter_for_strings")
    email = CharFilter(field_name="campus_email", method="global_filter_for_strings")
    search = CharFilter(
        field_name="search", method="global_search_for_strings_and_numbers"
    )

    class Meta:
        model = Campus
        fields = ["name", "email","search"]
