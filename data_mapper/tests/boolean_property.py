from unittest import TestCase

from data_mapper.properties.boolean import BooleanProperty


class BooleanPropertyTests(TestCase):
    def _test(self, prop, data, expected):
        result = prop.get(data)
        self.assertEqual(expected, result)

    def test__bool(self):
        self._test(
            prop=BooleanProperty('x'),
            data=dict(x=True),
            expected=True,
        )
        self._test(
            prop=BooleanProperty('x'),
            data=dict(x=False),
            expected=False,
        )

    def test__str(self):
        self._test(
            prop=BooleanProperty('x'),
            data=dict(x=''),
            expected=False,
        )
        self._test(
            prop=BooleanProperty('x'),
            data=dict(x='asdf'),
            expected=True,
        )
        self._test(
            prop=BooleanProperty('x'),
            data=dict(x='False'),
            expected=True,
        )

    def test__bool_fn(self):
        def first_uppercase(s: str):
            return len(s) > 0 and s[0].isupper()

        prop = BooleanProperty('x', bool_fn=first_uppercase)
        self._test(
            prop=prop,
            data=dict(x='ian'),
            expected=False,
        )
        self._test(
            prop=prop,
            data=dict(x='Ian'),
            expected=True,
        )
        self._test(
            prop=prop,
            data=dict(x=''),
            expected=False,
        )

    def test__true_values(self):
        prop = BooleanProperty(
            'x',
            true_values={'y', 'yes'},
            transforms=[str.lower],
        )
        self._test(
            prop=prop,
            data=dict(x=''),
            expected=False,
        )
        self._test(
            prop=prop,
            data=dict(x='Y'),
            expected=True,
        )
        self._test(
            prop=prop,
            data=dict(x='y'),
            expected=True,
        )
        self._test(
            prop=prop,
            data=dict(x='Yes'),
            expected=True,
        )
        self._test(
            prop=prop,
            data=dict(x='yes'),
            expected=True,
        )
        self._test(
            prop=prop,
            data=dict(x='no'),
            expected=False,
        )
