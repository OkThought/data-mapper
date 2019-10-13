from unittest.mock import Mock

from data_mapper.errors import PropertyNotResolved
from data_mapper.properties.functional import FunctionProperty as F
from data_mapper.shortcuts import V, P
from data_mapper.tests.test_utils import PropertyTestCase, NO_ASSERT


class FunctionPropertyTests(PropertyTestCase):
    def test__no_args__no_kwargs(self):
        self.prop_test(F(lambda: 1), 1)
        self.prop_test(F(lambda: 2, args=V(())), 2)
        self.prop_test(F(lambda: 3, args=V(()), kwargs=V({})), 3)
        self.prop_test(F(lambda: 4, kwargs=V({})), 4)

    def test__args__list_value(self):
        fun = Mock()
        self.prop_test(F(fun, args=V([1, 2])), NO_ASSERT)
        fun.assert_called_with(1, 2)
        self.prop_test(F(fun, args=V([[1, 2]])), NO_ASSERT)
        fun.assert_called_with([1, 2])
        self.prop_test(F(fun, args=V([[1, 2], 3])), NO_ASSERT)
        fun.assert_called_with([1, 2], 3)

    def test__args__values_list(self):
        fun = Mock()
        self.prop_test(F(fun, args=[V(1), V(2)]), NO_ASSERT)
        fun.assert_called_with(1, 2)
        self.prop_test(F(fun, args=[V([1, 2])]), NO_ASSERT)
        fun.assert_called_with([1, 2])
        self.prop_test(F(fun, args=[V([1, 2]), V(3)]), NO_ASSERT)
        fun.assert_called_with([1, 2], 3)

    def test__args__values_list__some_not_resolved(self):
        fun = Mock()
        self.prop_test(F(fun, args=[P(1)]), PropertyNotResolved)
        self.prop_test(F(fun, args=[P(1), V(2), V(3)]), PropertyNotResolved)
        self.prop_test(F(fun, args=[V(1), P(2), V(3)]), PropertyNotResolved)
        self.prop_test(F(fun, args=[V(1), V(2), P(3)]), PropertyNotResolved)

    def test__args__star_values(self):
        fun = Mock()
        self.prop_test(F(fun, V(1), V(2)), NO_ASSERT)
        fun.assert_called_with(1, 2)
        self.prop_test(F(fun, V([1, 2])), NO_ASSERT)
        fun.assert_called_with([1, 2])
        self.prop_test(F(fun, V([1, 2]), V(3)), NO_ASSERT)
        fun.assert_called_with([1, 2], 3)

    def test__args__star_values__some_not_resolved(self):
        fun = Mock()
        self.prop_test(F(fun, P(0), P(1)), PropertyNotResolved)
        self.prop_test(F(fun, P(0), P(1)), PropertyNotResolved)
        self.prop_test(F(fun, P(0), P(1)), PropertyNotResolved)

    def test__kwargs(self):
        fun = Mock()
        self.prop_test(F(fun), NO_ASSERT)
        fun.assert_called_with()
        self.prop_test(F(fun, kwargs=V(dict())), NO_ASSERT)
        fun.assert_called_with()
        self.prop_test(F(fun, kwargs=V(dict(x=1))), NO_ASSERT)
        fun.assert_called_with(x=1)
        self.prop_test(F(fun, kwargs=dict(x=V(1))), NO_ASSERT)
        fun.assert_called_with(x=1)
