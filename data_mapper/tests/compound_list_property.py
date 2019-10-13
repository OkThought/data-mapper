from data_mapper.properties import Property
from data_mapper.properties.compound_list import CompoundListProperty as L
from data_mapper.shortcuts import V, P
from data_mapper.tests.test_utils import PropertyTestCase


class CompoundListPropertyTests(PropertyTestCase):
    def test__simple(self):
        self.prop_test(L(V(1), V(2)), [1, 2])

    def test__empty(self):
        self.prop_test(L(), [])

    def test__props_it(self):
        self.prop_test(L(props_it=[V(1), V(2)]), [1, 2])
        self.prop_test(L(props_it=[V(1), V([2, 3])]), [1, [2, 3]])

    def test__star_props(self):
        self.prop_test(L(V(0)), [0])
        self.prop_test(L(V(0), V(1)), [0, 1])
        self.prop_test(L(V(0), V(1), V(2)), [0, 1, 2])
        self.prop_test(L(V(0), V(1), V(2)), [0, 1, 2])

    def test__star_props__some_not_resolved(self):
        self.prop_not_resolved(L(P(0)))
        self.prop_not_resolved(L(P(0), V(1)))
        self.prop_not_resolved(L(V(0), P(1)))
        self.prop_not_resolved(L(V(0), V(1), P(2)))
        self.prop_not_resolved(L(P(0), P(1), P(2)))

    def test__star_props__lists(self):
        self.prop_test(L([V(0), P(1)]), [0])
        self.prop_test(L([P(0), V(1)]), [1])
        self.prop_test(L([P(0), V(1)], [V(2)]), [1, 2])
        self.prop_test(L([P(0), V(1)], [P(2), V(3)]), [1, 3])

    def test__star_props__lists__some_entirely_not_resolved(self):
        self.prop_not_resolved(L([P(0)]))
        self.prop_not_resolved(L([P(0), P(1)]))
        self.prop_not_resolved(L([P(0), V(1)], [P(2)]))

    def test__get_value__set_in_parent(self):
        prop = L(
            Property('x'),
            get_value=lambda *_: 'foo',
        )
        self.prop_test(prop, ['foo'], dict(x=5))

    def test__get_value__set_in_grand_parent(self):
        prop = L(
            L(Property('x')),
            get_value=lambda *_: 'foo',
        )
        self.prop_test(prop, [['foo']], dict(x=5))
