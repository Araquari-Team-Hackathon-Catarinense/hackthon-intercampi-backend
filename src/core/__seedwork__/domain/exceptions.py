from rest_framework.exceptions import APIException


class CompanyNotInHeader(APIException):
    status_code = 401
    default_detail = "Campus não informado no cabeçalho."
    default_code = "company_not_in_header"
