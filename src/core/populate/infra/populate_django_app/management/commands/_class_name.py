from core.campus.infra.campus_django_app.models import Campus, ClassName
from core.populate.infra.resources.data_class_name import data_class_name_data


def populate_class_name() -> None:
    if ClassName.objects.exists():
        return

    campuses = [campus for campus in Campus.objects.all()]
    
    class_name_to_create: list[ClassName] = []

    for i, data in enumerate(data_class_name_data):
        campus = campuses[i % len(campuses)]
        class_name = ClassName(campus=campus, **data)
        class_name_to_create.append(class_name)

        

    if class_name_to_create:
        ClassName.objects.bulk_create(class_name_to_create)
        print("Class names created successfully.")
    else:
        print("Nenhum ClassName foi criado. Verifique os dados de entrada.")
