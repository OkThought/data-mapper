from data_mapper.properties.functional import FunctionProperty
from data_mapper.shortcuts import V
from data_mapper.tests.test_utils import PropertyTests


class FunctionPropertyTests(PropertyTests):
    def _test(self, expected, prop, data=None, raises=None):
        if data is None:
            data = {}
        if raises is not None:
            with self.assertRaises(raises):
                prop.get(data)
        else:
            self.assertEqual(expected, prop.get(data))

    def test__no_args__no_kwargs(self):
        self._test(1, FunctionProperty(lambda: 1))
        self._test(2, FunctionProperty(lambda: 2, args=V(())))
        self._test(3, FunctionProperty(lambda: 3, args=V(()), kwargs=V({})))
        self._test(4, FunctionProperty(lambda: 4, kwargs=V({})))

    def test__args(self):
        self._test(3, FunctionProperty(sum, args=V([[1, 2]])))
        self._test(6, FunctionProperty(sum, args=V([[1, 2], 3])))

    def test__kwargs(self):
        self._test(0, FunctionProperty(lambda *, x=0: x))
        self._test(0, FunctionProperty(lambda *, x=0: x, kwargs=V(dict())))
        self._test(1, FunctionProperty(lambda *, x=0: x, kwargs=V(dict(x=1))))
