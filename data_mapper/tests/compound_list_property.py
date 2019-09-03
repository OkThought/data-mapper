from data_mapper.errors import ValidationError
from data_mapper.properties import Property
from data_mapper.properties.compound_list import CompoundListProperty
from data_mapper.shortcuts import V
from data_mapper.tests.test_utils import PropertyTests


class CompoundListPropertyTests(PropertyTests):
    def test__simple(self):
        self.assertEqual([1, 2], CompoundListProperty(V(1), V(2)).get({}))

    def test__empty(self):
        self.assertEqual([], CompoundListProperty().get({}))

    def test__get_value__set_in_parent(self):
        prop = CompoundListProperty(
            Property('x'),
            get_value=lambda *_: 'foo',
        )
        self.assertEqual(['foo'], prop.get(dict(x=5)))

    def test__get_value__set_in_grand_parent(self):
        prop = CompoundListProperty(
            CompoundListProperty(Property('x')),
            get_value=lambda *_: 'foo',
        )
        self.assertEqual([['foo']], prop.get(dict(x=5)))
