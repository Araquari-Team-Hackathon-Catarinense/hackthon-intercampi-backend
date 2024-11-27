from core.class_name.infra.class_django_app.models import ClassName
from core.populate.infra.resources.data_class_name import data_class_name_data



def populate_class_name():
    for item in data_class_name_data:
        name = item.get("name")
        free_afternoons = item.get("free_afternoons", [])
        free_lunch = item.get("free_lunch", False)

        # Cria ou atualiza os registros no banco
        class_obj, created = ClassName.objects.get_or_create(
            name=name,
            defaults={
                "free_afternoons": free_afternoons,
                "free_lunch": free_lunch,
            },
        )

        if created:
            print(f"ClassName '{name}' foi criada com sucesso.")
        else:
            print(f"ClassName '{name}' já existia e não foi alterada.")