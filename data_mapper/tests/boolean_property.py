from data_mapper.properties import StringProperty
from data_mapper.properties.boolean import BooleanProperty
from data_mapper.shortcuts import F
from data_mapper.tests.test_utils import PropertyTests


class BooleanPropertyTests(PropertyTests):
    def test__bool(self):
        self.prop_test(
            prop=BooleanProperty('x'),
            data=dict(x=True),
            expect=True,
        )
        self.prop_test(
            prop=BooleanProperty('x'),
            data=dict(x=False),
            expect=False,
        )

    def test__str(self):
        self.prop_test(
            prop=BooleanProperty('x'),
            data=dict(x=''),
            expect=False,
        )
        self.prop_test(
            prop=BooleanProperty('x'),
            data=dict(x='asdf'),
            expect=True,
        )
        self.prop_test(
            prop=BooleanProperty('x'),
            data=dict(x='False'),
            expect=True,
        )

    def test__bool_fn(self):
        def first_uppercase(s: str):
            return len(s) > 0 and s[0].isupper()

        prop = BooleanProperty(StringProperty('x'), bool_fn=first_uppercase)
        self.prop_test(
            prop=prop,
            data=dict(x='ian'),
            expect=False,
        )
        self.prop_test(
            prop=prop,
            data=dict(x='Ian'),
            expect=True,
        )
        self.prop_test(
            prop=prop,
            data=dict(x=''),
            expect=False,
        )

    def test__true_values(self):
        prop = BooleanProperty(
            F(str.lower, [StringProperty('x')]),
            true_values={'y', 'yes'},
        )
        self.prop_test(
            prop=prop,
            data=dict(x=''),
            expect=False,
        )
        self.prop_test(
            prop=prop,
            data=dict(x='Y'),
            expect=True,
        )
        self.prop_test(
            prop=prop,
            data=dict(x='y'),
            expect=True,
        )
        self.prop_test(
            prop=prop,
            data=dict(x='Yes'),
            expect=True,
        )
        self.prop_test(
            prop=prop,
            data=dict(x='yes'),
            expect=True,
        )
        self.prop_test(
            prop=prop,
            data=dict(x='no'),
            expect=False,
        )

    def test__default(self):
        self.prop_test(
            prop=BooleanProperty('x', default=True),
            data=dict(),
            expect=True,
        )
        self.prop_test(
            prop=BooleanProperty('x', default=False),
            data=dict(),
            expect=False,
        )
