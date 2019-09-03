from data_mapper.properties.functional import FunctionProperty
from data_mapper.shortcuts import V
from data_mapper.tests.test_utils import PropertyTests


class FunctionPropertyTests(PropertyTests):
    def test__no_args__no_kwargs(self):
        self.prop_test(FunctionProperty(lambda: 1), 1)
        self.prop_test(FunctionProperty(lambda: 2, args=V(())), 2)
        self.prop_test(FunctionProperty(lambda: 3, args=V(()), kwargs=V({})), 3)
        self.prop_test(FunctionProperty(lambda: 4, kwargs=V({})), 4)

    def test__args__list_value(self):
        self.prop_test(FunctionProperty(sum, args=V([[1, 2]])), 3)
        self.prop_test(FunctionProperty(sum, args=V([[1, 2], 3])), 6)

    def test__args__values_list(self):
        self.prop_test(FunctionProperty(sum, args=[V([1, 2])]), 3)
        self.prop_test(FunctionProperty(sum, args=[V([1, 2]), V(3)]), 6)

    def test__args__star_values(self):
        self.prop_test(FunctionProperty(sum, V([1, 2])), 3)
        self.prop_test(FunctionProperty(sum, V([1, 2]), V(3)), 6)

    def test__kwargs(self):
        self.prop_test(FunctionProperty(lambda *, x=0: x), 0)
        self.prop_test(FunctionProperty(lambda *, x=0: x, kwargs=V(dict())), 0)
        self.prop_test(
            FunctionProperty(lambda *, x=0: x, kwargs=V(dict(x=1))), 1)
        self.prop_test(
            FunctionProperty(lambda *, x=0: x, kwargs=dict(x=V(1))), 1)
