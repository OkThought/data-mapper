from unittest import TestCase

from data_mapper.mappers.object import ObjectMapper
from data_mapper.properties.compound_list import CompoundListProperty
from data_mapper.properties.integer import IntegerProperty
from data_mapper.properties.string import StringProperty


class Person:
    def __init__(
            self,
            id_: int,
            first_name: str,
            last_name: str,
            middle_name: str = None,
    ):
        self.id = id_
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name

    def __eq__(self, other):
        return (
                isinstance(other, Person) and
                self.id == other.id and
                self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.middle_name == other.middle_name
        )


class ObjectPropertyTests(TestCase):
    dostoevsky = Person(0, 'Fyodor', 'Dostoevsky', 'Mikhailovich')
    dostoevsky_dict = dict(
        id=dostoevsky.id,
        first_name=dostoevsky.first_name,
        middle_name=dostoevsky.middle_name,
        last_name=dostoevsky.last_name,
    )

    def test__subclass(self):
        class PersonMapper(ObjectMapper):
            init = Person
            args = CompoundListProperty(
                IntegerProperty('id'),
                StringProperty('first_name'),
                StringProperty('last_name'),
                StringProperty('middle_name', required=False),
                skip_none=True,
                allowed_sizes=range(3, 5),
            )

        self.assertEqual(
            self.dostoevsky,
            PersonMapper().get(self.dostoevsky_dict)
        )

    def test__init(self):
        person_mapper = ObjectMapper(
            init=Person,
            args=CompoundListProperty(
                IntegerProperty('id'),
                StringProperty('first_name'),
                StringProperty('last_name'),
                StringProperty('middle_name', required=False),
                skip_none=True,
                allowed_sizes=range(3, 5),
            ),
        )
        self.assertEqual(
            self.dostoevsky,
            person_mapper.get(self.dostoevsky_dict)
        )
