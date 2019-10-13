from data_mapper.shortcuts import V, P, D, R
from data_mapper.tests.test_utils import PropertyTestCase


class OperatorTests(PropertyTestCase):
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

    def test__get_item__index_out_of_range__with_default(self):
        self.prop_test(P(V([])[0], default=0), 0)
        self.prop_test(P(V([])[1], default=0), 0)
        self.prop_test(P(V([])[-1], default=0), 0)

    def test__ref__get_item__index_out_of_range__with_default(self):
        self.prop_test(D(a=V([]), x=P(R('a')[0], default=0))['x'], 0)
        self.prop_test(D(a=V([]), x=P(R('a')[1], default=0))['x'], 0)
        self.prop_test(D(
            dict(lazy=True),
            a=V([]),
            x=R('a')[1],
            y=R('x', default=0)
        )['y'], 0)
