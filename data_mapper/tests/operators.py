from data_mapper.shortcuts import V, P
from data_mapper.tests.test_utils import PropertyTests


class OperatorTests(PropertyTests):
    def test__and__first_false(self):
        self.prop_test(V(False) & P('absent'), False)

    def test__and__first_false_ish(self):
        self.assertIs(0, (V(0) & P('absent')).get({}))

    def test__and__first_true_ish(self):
        true_ish = [2]
        self.assertIs(true_ish, (V(1) & V(true_ish)).get({}))
        false_ish = []
        self.assertIs(false_ish, (V(1) & V(false_ish)).get({}))

    def test__or__first_true(self):
        self.prop_test(V(True) | P('absent'), True)

    def test__or__first_true_ish(self):
        self.assertIs(1, (V(1) | P('absent')).get({}))

    def test__or__first_false_ish(self):
        true_ish = [2]
        self.assertIs(true_ish, (V(0) | V(true_ish)).get({}))
        false_ish = []
        self.assertIs(false_ish, (V(0) | V(false_ish)).get({}))
