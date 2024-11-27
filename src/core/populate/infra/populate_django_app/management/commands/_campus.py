from core.campus.infra.campus_django_app.models import Campus
from core.populate.infra.resources.data_campus import campus_data

def populate_campus() -> None:
    print('socorro')
    if Campus.objects.exists():
        return
    
    print("foda-se")

    campus_to_create: list[Campus] = [Campus(**data) for data in campus_data]
    Campus.objects.bulk_create(campus_to_create)

