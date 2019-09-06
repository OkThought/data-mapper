from data_mapper.errors import PropertyNotResolved
from data_mapper.properties.integer import IntegerProperty
from data_mapper.tests.test_utils import PropertyTests


class IntegerPropertyTests(PropertyTests):
    def test__int(self):
        self.prop_test(
            prop=IntegerProperty('x'),
            data=dict(x=1),
            expect=1,
        )

    def test__str(self):
        self.prop_test(
            prop=IntegerProperty('x'),
            data=dict(x='1'),
            expect=1,
        )

    def test__str__empty(self):
        with self.assertRaises(PropertyNotResolved):
            self.prop_test(
                prop=IntegerProperty('x'),
                data=dict(x=''),
                expect=None,
            )
        self.prop_test(
            prop=IntegerProperty('x', default=None),
            data=dict(x=''),
            expect=None,
        )
        self.prop_test(
            prop=IntegerProperty('x', required=False),
            data=dict(x=''),
            expect=None,
        )

    def test__float(self):
        self.prop_test(
            prop=IntegerProperty('x'),
            data=dict(x=1.1),
            expect=1,
        )

    def test__none(self):
        self.prop_test(
            prop=IntegerProperty('x', required=False),
            data=dict(x=None),
            expect=None,
        )
        self.prop_test(
            prop=IntegerProperty('x', required=False),
            data=dict(),
            expect=None,
        )
