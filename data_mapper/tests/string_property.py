from data_mapper.mappers.mapper import Mapper
from data_mapper.properties.string import StringProperty
from data_mapper.tests.test_utils import PropertyTests


class StringPropertyTests(PropertyTests):
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
