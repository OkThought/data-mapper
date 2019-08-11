from unittest import TestCase

from data_mapper.mappers.mapper import Mapper
from data_mapper.properties.string import StringProperty


class StringPropertyTests(TestCase):
    def test__in_mapper(self):
        value, expected_value = 'hannah', 'hannah'

        class MyMapper(Mapper):
            name = StringProperty()

        mapper = MyMapper()
        self.assertEqual(
            dict(mapper.get(dict(name=value))),
            dict(name=expected_value),
        )

    def test__in_mapper__no_sources(self):
        value, expected_value = 'hannah', 'hannah'

        class MyMapper(Mapper):
            name = StringProperty()

        mapper = MyMapper()
        self.assertEqual(
            dict(mapper.get(dict(name=value))),
            dict(name=expected_value),
        )

    def test__numbers(self):
        prop = StringProperty(['n'])
        self.assertEqual(prop.get(dict(n=1)), '1')

    def test__transforms__capitalize(self):
        value, expected_value = 'hannah', 'Hannah'
        name = StringProperty(
            ['name'],
            required=True,
            transforms=[str.capitalize]
        )

        self.assertEqual(
            name.get(dict(name=value)),
            expected_value,
        )

    def test__transforms__strip(self):
        value, expected_value = ' hannah \t\r\n', 'hannah'
        name = StringProperty(
            ['name'],
            required=True,
            transforms=[str.strip]
        )

        self.assertEqual(
            name.get(dict(name=value)),
            expected_value,
        )

    def test__transforms__strip_chars(self):
        value, expected_value = '[hannah]', 'hannah'
        name = StringProperty(
            ['name'],
            required=True,
            transforms=[lambda s: s.strip('[]')]
        )

        self.assertEqual(
            name.get(dict(name=value)),
            expected_value,
        )
