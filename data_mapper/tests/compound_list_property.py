from data_mapper.errors import ValidationError
from data_mapper.properties import Property
from data_mapper.properties.compound_list import CompoundListProperty
from data_mapper.shortcuts import V, P
from data_mapper.tests.test_utils import PropertyTests


class CompoundListPropertyTests(PropertyTests):
    def test__simple(self):
        self.prop_test(CompoundListProperty(V(1), V(2)), [1, 2])

    def test__empty(self):
        self.prop_test(CompoundListProperty(), [])

    def test__props_it(self):
        self.prop_test(CompoundListProperty(props_it=[V(1), V(2)]), [1, 2])

    def test__invalid_followed_by_valid(self):
        self.prop_test(CompoundListProperty([P(0), V(1)]), [1])

    def test__get_value__set_in_parent(self):
        prop = CompoundListProperty(
            Property('x'),
            get_value=lambda *_: 'foo',
        )
        self.prop_test(prop, ['foo'], dict(x=5))

    def test__get_value__set_in_grand_parent(self):
        prop = CompoundListProperty(
            CompoundListProperty(Property('x')),
            get_value=lambda *_: 'foo',
        )
        self.prop_test(prop, [['foo']], dict(x=5))
