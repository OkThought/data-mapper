from unittest import TestCase

from data_mapper.properties.operations.operation import Operation
from data_mapper.properties.string import StringProperty


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
