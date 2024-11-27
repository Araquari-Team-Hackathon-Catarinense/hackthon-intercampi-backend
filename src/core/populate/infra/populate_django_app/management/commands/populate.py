# pylint: disable=no-member
from django.core.management.base import BaseCommand, CommandError, CommandParser

from core.populate.infra.populate_django_app.management.commands import (
    populate_employee,
    populate_users,
    populate_campus,
    populate_student,
    populate_class_name,
   
)

class Command(BaseCommand):
    help = "Populate the database with the initial data"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--campus",
            action="store_true",
            help="Populate the campus data",
        )
        parser.add_argument(
            "--users",
            action="store_true",
            help="Populate the users data",
        )
        parser.add_argument(
            "--all", action="store_true", help="Populate all data available"
        )

    def handle(self, *args, **options):
        try:
            if options.get("all"):
                self.__handle_all()
            if options.get("campus"):
                self.__handle_campus()
            if options.get("users"):
                self.__handle_users()
            if options.get("employee"):
                self.__handle_employee()
            if options.get("student"):
                self.__handle_student()
            if options.get("class_name"):
                self.__handle_class()

       

            self.stdout.write(self.style.SUCCESS("\nTudo populado com sucesso! :D"))
        except CommandError as exc:
            raise CommandError(f"An error occurred: {exc}") from exc
        except Exception as e:
            raise CommandError(f"An error occurred: {e}") from e

    def __handle_campus(self):
        self.stdout.write("Populating campus data...", ending="")
        populate_campus()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_users(self):
        self.stdout.write("Populating users data...", ending="")
        populate_users()    
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_class(self):
        self.stdout.write("Populating class data...", ending="")
        populate_class_name()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_employee(self):
        self.stdout.write("Populating employees data...", ending="")
        populate_employee()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_student(self):
        self.stdout.write("Populating student data...", ending="")
        populate_student()
        self.stdout.write(self.style.SUCCESS("OK"))

    def __handle_all(self):
        self.stdout.write("Populating all data...", ending="")
        self.__handle_campus()
        self.__handle_class()
        self.__handle_users()
        self.__handle_employee()
        self.__handle_student()

        
       
        self.stdout.write(self.style.SUCCESS("OK"))
