from data_mapper.shortcuts import V, P
from data_mapper.tests.test_utils import PropertyTests


class OperatorTests(PropertyTests):
    def test__and__first_false(self):
        self.prop_test(V(False) & P('absent'), False)

    def test__or__first_true(self):
        self.prop_test(V(True) | P('absent'), True)
