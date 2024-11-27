import random

from core.campus.infra.campus_django_app.models import Campus, Employee, Student, ClassName
from core.populate.infra.resources.data_user import drivers_data, users_data
from core.user.infra.user_django_app.models import User

from faker import Faker

fake = Faker("pt_BR")


def populate_users() -> None:
    if User.objects.exists():
        return

    users_to_create: list[User] = [User(**data) for data in users_data]
    User.objects.bulk_create(users_to_create)
    for user in users_to_create:
        user.set_password(user.password)
        user.save()


# def populate_drivers() -> None:
#     if Driver.objects.exists():
#         return
#     if User.objects.exists():
#         drivers_to_create: list[Driver] = [Driver(**data) for data in drivers_data]
#         Driver.objects.bulk_create(drivers_to_create)


def populate_employee() -> None:
    if not Campus.objects.exists():
        print("No companies found. Populate companies first.")
        return

    if not User.objects.exists():
        print("No users found. Populate users first.")
        return

    companies = list(Campus.objects.all())
    users = list(User.objects.all())

    print("Creating employees...")
    employees_to_create = []

    for _ in range(35):
        company = random.choice(companies)
        user = random.choice(users) 
        siape = fake.pyint(min_value=11111111111, max_value=99999999999)

        employee = Employee(campus=company, user=user, siape=siape)
        employees_to_create.append(employee)

    Employee.objects.bulk_create(employees_to_create)
    print("Employees created successfully.")


def populate_student() -> None:
    if not Campus.objects.exists():
        print("No companies found. Populate companies first.")
        return

    if not User.objects.exists():
        print("No users found. Populate users first.")
        return

    companies = list(Campus.objects.all())
    users = list(User.objects.all())
    class_name = list(ClassName.objects.all())

    print("Creating employees...")
    employees_to_create = []

    for _ in range(35):
        company = random.choice(companies)
        user = random.choice(users) 
        siape = fake.pyint(min_value=11111111111, max_value=99999999999)

        employee = Student(user=user, registration=siape)
        employees_to_create.append(employee)

    Student.objects.bulk_create(employees_to_create)
    print("Employees created successfully.")
