from unittest import TestCase


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
