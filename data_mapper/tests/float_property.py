from unittest import TestCase

from data_mapper.errors import PropertyNotFound
from data_mapper.properties.float import FloatProperty


class FloatPropertyTests(TestCase):
    def _test(self, prop, data, expected):
        result = prop.get(data)
        self.assertEqual(expected, result)

    def test__int(self):
        self._test(
            prop=FloatProperty('x'),
            data=dict(x=1),
            expected=1.,
        )

    def test__str(self):
        self._test(
            prop=FloatProperty('x'),
            data=dict(x='1.'),
            expected=1.,
        )

    def test__str__empty(self):
        with self.assertRaises(PropertyNotFound):
            self._test(
                prop=FloatProperty('x'),
                data=dict(x=''),
                expected=None,
            )
        self._test(
            prop=FloatProperty('x', default=None),
            data=dict(x=''),
            expected=None,
        )
        self._test(
            prop=FloatProperty('x', required=False),
            data=dict(x=''),
            expected=None,
        )

    def test__float(self):
        self._test(
            prop=FloatProperty('x'),
            data=dict(x=1.1),
            expected=1.1,
        )

    def test__none(self):
        self._test(
            prop=FloatProperty('x', required=False),
            data=dict(x=None),
            expected=None,
        )
        self._test(
            prop=FloatProperty('x', required=False),
            data=dict(),
            expected=None,
        )
