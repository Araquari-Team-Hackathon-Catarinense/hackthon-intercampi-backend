import random
import re
import uuid

from faker import Faker
from pycpfcnpj import gen

faker = Faker("pt_BR")


# def generate_cpf():
#     return re.sub("[^0-9]", "", gen.cpf())


# def generate_cnpj():
#     return re.sub("[^0-9]", "", gen.cnpj())


# def generate_address():
#     return {
#         "zip_code": re.sub("[^0-9]", "", faker.postcode()),
#         "address": faker.street_address(),
#         "number": random.randint(1, 9999),
#         "district": faker.bairro(),
#         "city_name": faker.city(),
#         "city_ibge_code": faker.random_number(digits=7),
#         "state_acronym": faker.state_abbr(),
#         "state_ibge_code": faker.random_number(digits=7),
#     }


# def generate_contacts(index, type):
#     return [
#         {
#             "name": faker.name(),
#             "phone": re.sub("[^0-9]", "", faker.phone_number()),
#             "email": f"{type}{index}.admin@example.com",
#             "obs": "Administrativo",
#         }
#     ]


# def generate_companies():
#     companies = []

#     for index in range(10):
#         index += 1
#         company_pj = {
#             "id": str(uuid.uuid4()),
#             "name": f"Empresa {index}",
#             "trade_name": f"Nome Fantasia {index}",
            
#         }
#         companies.append(company_pj)

#     for index in range(10):
#         index += 1
#         company_pf = {
#             "id": str(uuid.uuid4()),
#             "name": faker.name(),
#             "trade_name": None,
#             "person_type": "PF",
#             "document_number": generate_cpf(),
#             "is_active": True,
#             "system_admin": False,
#             "address": generate_address(),
#             "contacts": generate_contacts(index, "pf"),
#         }
#         companies.append(company_pf)

#     return companies


# companies_json = generate_companies()

# import json

# print(json.dumps(companies_json, indent=4, ensure_ascii=False))


valid_uuids = [str(uuid.uuid4()) for _ in range(10)]

campus_data = [
    {
        "id": valid_uuids[0],
        "name": "Campus Araquari",
        "email": "ifcaraquari@ifc.edu.br"
    },
    {
        "id": valid_uuids[1],
        "name": "Campus São Bento do Sul",
        "email": "ifcsaobentodosul@ifc.edu.br"
    },
    {
        "id": valid_uuids[2],
        "name": "Campus Concórdia",
        "email": "ifcconcordia@ifc.edu.br"
    },
    {
        "id": valid_uuids[3],
        "name": "Campus Brusque",
        "email": "ifcbrusque@ifc.edu.br"
    },
    {
        "id": valid_uuids[4],
        "name": "Campus Blumenau",
        "email": "ifcblumenau@ifc.edu.br"
    },
]
