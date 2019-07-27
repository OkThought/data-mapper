from unittest import TestCase

from src.mappers.base import Mapper
from src.properties.string import StringProperty


class Tests(TestCase):
    def test__string_property__transforms(self):
        value, expected_value = 'hannah', 'Hannah'

        class MyMapper(Mapper):
            name = StringProperty(
                required=True,
                transforms=[str.capitalize]
            )

        mapper = MyMapper()
        self.assertEqual(
            dict(mapper.map(dict(name=value))),
            dict(name=expected_value),
        )
