from django.shortcuts import render
from django.db import connection, reset_queries

from .models import PetSitter, Pet

# Create your views here.


def get_sql_queries(origin_func):
    def wrapper(*args, **kwargs):
        reset_queries()
        origin_func()
        query_info = connection.queries
        for query in query_info:
            print(query["sql"])

    return wrapper


@get_sql_queries
def get_pet_data():
    pets = Pet.objects.all().select_related("pet_sitter")
    for pet in pets:
        print(f"{pet.name} | 집사 {pet.pet_sitter.first_name}")


########################################################################
################아래 함수를 윗 함수처럼 데코레이터로 사용 가능##############
########################################################################
# def get_pet_data():
#     pets = Pet.objects.all()
#     for pet in pets:
#         print(f"{pet.name} | 집사 {pet.pet_sitter.first_name}")

#     query_info = connection.queries
#     for query in query_info:
#         print(query["sql"])
