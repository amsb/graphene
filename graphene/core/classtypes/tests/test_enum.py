from graphql.core.type import GraphQLEnumType

from graphene.core.schema import Schema

from ..enum import Enum


def test_enum():
    class RGB(Enum):
        '''RGB enum description'''
        RED = 0
        GREEN = 1
        BLUE = 2

    schema = Schema()

    object_type = schema.T(RGB)
    assert isinstance(object_type, GraphQLEnumType)
    assert RGB._meta.type_name == 'RGB'
    assert RGB._meta.description == 'RGB enum description'
    assert RGB.RED == 0
    assert RGB.GREEN == 1
    assert RGB.BLUE == 2


def test_enum_values():
    RGB = Enum('RGB', dict(RED=0, GREEN=1, BLUE=2), description='RGB enum description')

    schema = Schema()

    object_type = schema.T(RGB)
    assert isinstance(object_type, GraphQLEnumType)
    assert RGB._meta.type_name == 'RGB'
    assert RGB._meta.description == 'RGB enum description'
    assert RGB.RED == 0
    assert RGB.GREEN == 1
    assert RGB.BLUE == 2
