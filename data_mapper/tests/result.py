from unittest import TestCase

from data_mapper.mappers.mapper import Mapper
from data_mapper.properties.string import StringProperty
from data_mapper.result import MapResult
from data_mapper.shortcuts import V


class MapResultTests(TestCase):
    def test__double_star_unpacking(self):
        class MyMapper(Mapper):
            first_name = StringProperty(['name'])
            last_name = StringProperty(['surname'])
        mapper = MyMapper()
        name, surname = 'Ivan Bogush'.split()
        result = mapper.get(dict(name=name, surname=surname))
        self.assertEqual(
            dict(first_name=name, last_name=surname),
            dict(**result),
        )

    def test__evaluate(self):
        result = MapResult(dict(x=V(1)), {})
        result.evaluate()
        self.assertEqual(dict(x=1), result.cache)

    def test__not_lazy(self):
        result = MapResult(dict(x=V(1)), {}, lazy=False)
        self.assertEqual(dict(x=1), result.cache)
