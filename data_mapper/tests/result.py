from unittest import TestCase
from unittest.mock import Mock

from data_mapper.result import MapResult
from data_mapper.shortcuts import V, P


class MapResultTests(TestCase):
    def test__double_star_unpacking__lazy(self):
        self.assertEqual(dict(x=1), {**MapResult(dict(x=V(1)), {}, lazy=True)})

    def test__double_star_unpacking__not_lazy(self):
        self.assertEqual(dict(x=1), {**MapResult(dict(x=V(1)), {}, lazy=False)})

    def test__evaluate__lazy(self):
        result = MapResult(dict(x=V(1)), {}, lazy=True)
        result.evaluate()
        self.assertEqual(dict(x=1), result.cache)

    def test__evaluate__not_lazy(self):
        result = MapResult(dict(x=V(1)), {}, lazy=False)
        result.evaluate()
        self.assertEqual(dict(x=1), result.cache)

    def test__cache__lazy(self):
        result = MapResult(dict(x=V(1)), {}, lazy=True)
        self.assertEqual(dict(), result.cache)

    def test__cache__not_lazy(self):
        result = MapResult(dict(x=V(1)), {}, lazy=False)
        self.assertEqual(dict(x=1), result.cache)
