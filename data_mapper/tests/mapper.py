from unittest import TestCase

from data_mapper.mappers.mapper import Mapper
from data_mapper.properties import Property
from data_mapper.properties.string import StringProperty


class MapperTests(TestCase):
    def test__properties__get_absent(self):
        mapper = Mapper()
        result = mapper.get(dict(a=1))
        with self.assertRaises(KeyError):
            # noinspection PyStatementEffect
            result['a']

    def test__mapper_as_a_property(self):
        class PersonId(Mapper):
            first_name = StringProperty('first_name', 'name')
            last_name = StringProperty('last_name', 'surname', 'family_name')

        class Person(Mapper):
            id = PersonId(dict(sources=None))

        person = Person()
        first_name = 'Bob'
        last_name = 'Marley'
        self.assertEqual(
            dict(
                id=dict(
                    first_name=first_name,
                    last_name=last_name,
                )
            ),
            person.get(dict(
                id=dict(
                    name=first_name,
                    surname=last_name,
                ),
            )),
        )

    def test__get_value__set_in_parent(self):
        prop = Mapper(
            dict(get_value=lambda *_: 'foo'),
            x=Property(),
        )
        self.assertEqual('foo', prop.get(dict(x=5))['x'])

    def test__get_value__set_in_grand_parent(self):
        prop = Mapper(
            dict(get_value=lambda *_: 'foo'),
            y=Mapper(
                x=Property(),
            ),
        )
        self.assertEqual('foo', prop.get(dict(x=5))['y']['x'])
