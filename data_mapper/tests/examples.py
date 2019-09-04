from datetime import date
from unittest import TestCase

from data_mapper.mappers import Mapper
from data_mapper.mappers.object import ObjectMapper
from data_mapper.properties.compound import CompoundProperty
from data_mapper.properties.compound_list import CompoundListProperty
from data_mapper.properties.integer import IntegerProperty
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
        from data_mapper.shortcuts import F, Str, L

        full_name = F(
            ' '.join,
            L(
                Str('first_name'),
                Str('middle_name', required=False),
                Str('last_name'),
                skip_none=True,
            ),
        )

        assert 'Anton Pavlovich Chekhov' == full_name.get(dict(
            first_name='Anton',
            middle_name='Pavlovich',
            last_name='Chekhov',
        ))

        assert 'Anton Chekhov' == full_name.get(dict(
            first_name='Anton',
            last_name='Chekhov',
        ))

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

    def test__object_to_dict(self):
        mapper = Mapper(
            year=IntegerProperty(),
            month=IntegerProperty(),
            day=IntegerProperty(),
        )

        d = date(year=1997, month=4, day=12)
        value = mapper.get(d)
        self.assertEqual(
            dict(year=d.year, month=d.month, day=d.day),
            dict(value),
        )
