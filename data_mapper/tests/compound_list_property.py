from unittest import TestCase

from data_mapper.errors import ValidationError
from data_mapper.properties import Property
from data_mapper.properties.compound_list import CompoundListProperty
from data_mapper.properties.value import V


class CompoundListPropertyTests(TestCase):
    def test__simple(self):
        self.assertEqual([1, 2], CompoundListProperty(V(1), V(2)).get({}))

    def test__empty(self):
        self.assertEqual([], CompoundListProperty().get({}))

    def test__allowed_sizes__range(self):
        prop = CompoundListProperty(
            Property('x'),
            Property('y', required=False),
            Property('z', required=False),
            allowed_sizes=range(2, 4),
            skip_none=True,
        )

        with self.assertRaises(ValidationError):
            value = prop.get(dict(x=1))
            self.assertTrue(value and False, msg=value)

        self.assertEqual([1, 2, 3], prop.get(dict(x=1, y=2, z=3)))
        self.assertEqual([1, 2], prop.get(dict(x=1, y=2)))
        self.assertEqual([1, 2], prop.get(dict(x=1, z=2)))
