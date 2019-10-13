from data_mapper.errors import PropertyNotResolved
from data_mapper.shortcuts import D, V, R
from data_mapper.tests.test_utils import PropertyTestCase


class PropertyRefTests(PropertyTestCase):
    def test__empty_source(self):
        with self.assertRaises(PropertyNotResolved):
            R().get({}, {})
        with self.assertRaises(PropertyNotResolved):
            R(sources_it=[]).get({}, {})
        self.prop_test(D(x=V(1), y=D(x=R()))['y']['x'], 1)

    def test__source(self):
        self.prop_test(R(1), 9, result={1: 9})

    def test__sources(self):
        self.prop_test(R(1, 2), 9, result={2: 9})

    def test__sources_it(self):
        self.prop_test(R(sources_it=[1, 2]), 9, result={2: 9})
        self.prop_test(R(sources_it=[[1, 2]]), 9, result={1: {2: 9}})

    def test__source__list(self):
        self.prop_test(R([1]), 9, result={1: 9})
        self.prop_test(R([1, 2]), 9, result={1: {2: 9}})

    def test__sources__lists(self):
        self.prop_test(R([2, 1], [1, 3], [1, 2]), 9, result={1: {2: 9}})

    def test__default(self):
        self.prop_test(R(default=9), 9, result={})

    def test__result__list(self):
        self.prop_test(R(0), 9, result=[9])

    def test__ref_to_property_in_parent(self):
        self.prop_test(D(x=V(1), y=R('x'))['y'], 1)

    def test__ref_to_property_in_grandparent(self):
        self.prop_test(D(x=V(1), y=D(z=R('x')))['y']['z'], 1)
