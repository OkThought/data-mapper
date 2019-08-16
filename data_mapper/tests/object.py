from unittest import TestCase

from data_mapper.mappers.object import ObjectMapper
from data_mapper.properties.compound import CompoundProperty
from data_mapper.properties.compound_list import CompoundListProperty
from data_mapper.properties.integer import IntegerProperty
from data_mapper.properties.string import StringProperty
from data_mapper.tests.test_utils import Person


class ObjectPropertyTests(TestCase):
    dostoevsky = Person(0, 'Fyodor', 'Dostoevsky', 'Mikhailovich')
    dostoevsky_no_middle_name = Person(0, 'Fyodor', 'Dostoevsky')
    dostoevsky_dict = dict(
        id=dostoevsky.id,
        first_name=dostoevsky.first_name,
        middle_name=dostoevsky.middle_name,
        last_name=dostoevsky.last_name,
    )
    dostoevsky_no_middle_name_dict = dict(
        id=dostoevsky.id,
        first_name=dostoevsky.first_name,
        last_name=dostoevsky.last_name,
    )

    def test__subclass__args(self):
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
        self.assertEqual(
            self.dostoevsky_no_middle_name,
            PersonMapper().get(self.dostoevsky_no_middle_name_dict)
        )

    def test__subclass__args_kwargs(self):
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

        self.assertEqual(
            self.dostoevsky,
            PersonMapper().get(self.dostoevsky_dict)
        )
        self.assertEqual(
            self.dostoevsky_no_middle_name,
            PersonMapper().get(self.dostoevsky_no_middle_name_dict)
        )

    def test__init__args(self):
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
        self.assertEqual(
            self.dostoevsky_no_middle_name,
            person_mapper.get(self.dostoevsky_no_middle_name_dict)
        )

    def test__init__args_kwargs(self):
        person_mapper = ObjectMapper(
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

        self.assertEqual(
            self.dostoevsky,
            person_mapper.get(self.dostoevsky_dict)
        )
        self.assertEqual(
            self.dostoevsky_no_middle_name,
            person_mapper.get(self.dostoevsky_no_middle_name_dict)
        )
