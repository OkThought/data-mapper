from unittest import TestCase

from data_mapper.mappers.object import ObjectMapper
from data_mapper.properties.compound import CompoundProperty
from data_mapper.properties.compound_list import CompoundListProperty
from data_mapper.properties.integer import IntegerProperty
from data_mapper.properties.operations.operation import Operation
from data_mapper.properties.string import StringProperty
from data_mapper.tests.test_utils import Person


class ExamplesTests(TestCase):
    def test__different_naming_schemes(self):
        from data_mapper.mappers import Mapper
        from data_mapper.properties import Property

        class PersonMapper(Mapper):
            first_name = Property('first_name', 'name')
            last_name = Property('last_name', 'surname')

        mapper = PersonMapper()

        self.assertEqual(mapper.get({
            'first_name': 'Ivan',
            'surname': 'Bogush',
        }), {
            'first_name': 'Ivan',
            'last_name': 'Bogush',
        })

        self.assertEqual(mapper.get({
            'name': 'Ivan',
            'surname': 'Bogush',
        }), {
            'first_name': 'Ivan',
            'last_name': 'Bogush',
        })

    def test__full_name(self):
        full_name = Operation(
            StringProperty('first_name'),
            StringProperty('middle_name', required=False),
            StringProperty('last_name'),
            func=lambda args: ' '.join(filter(None, args)),
        )

        self.assertEqual(
            'Anton Pavlovich Chekhov',
            full_name.get(dict(
                first_name='Anton',
                middle_name='Pavlovich',
                last_name='Chekhov',
            )),
        )

        self.assertEqual(
            'Anton Chekhov',
            full_name.get(dict(
                first_name='Anton',
                last_name='Chekhov',
            )),
        )

    @staticmethod
    def test__object_mapper__subclass():
        class PersonMapper(ObjectMapper):
            init = Person
            args = CompoundListProperty(
                IntegerProperty('id'),
                StringProperty('first_name'),
                StringProperty('last_name'),
            )
            kwargs = CompoundProperty(
                middle_name=StringProperty(required=False),
            )

        first, middle, last = 'Iosif Aleksandrovich Brodsky'.split()
        person = PersonMapper().get(dict(
            id=1940,
            first_name=first,
            middle_name=middle,
            last_name=last,
        ))

        assert isinstance(person, Person)
        assert person.id == 1940
        assert person.first_name == first
        assert person.middle_name == middle
        assert person.last_name == last

    @staticmethod
    def test__object_mapper__init():
        mapper = ObjectMapper(
            init=Person,
            args=CompoundListProperty(
                IntegerProperty('id'),
                StringProperty('first_name'),
                StringProperty('last_name'),
            ),
            kwargs=CompoundProperty(
                middle_name=StringProperty(required=False),
            ),
        )

        first, middle, last = 'Iosif Aleksandrovich Brodsky'.split()
        person = mapper.get(dict(
            id=1940,
            first_name=first,
            middle_name=middle,
            last_name=last,
        ))

        assert isinstance(person, Person)
        assert person.id == 1940
        assert person.first_name == first
        assert person.middle_name == middle
        assert person.last_name == last
