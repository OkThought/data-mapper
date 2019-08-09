from unittest import TestCase

from src.mappers.mapper import Mapper
from src.properties.string import StringProperty


class MapResultTests(TestCase):
    def test__double_star_unpacking(self):
        class MyMapper(Mapper):
            first_name = StringProperty(['name'])
            last_name = StringProperty(['surname'])
        mapper = MyMapper()
        name, surname = 'Ivan Bogush'.split()
        result = mapper.map(dict(name=name, surname=surname))
        self.assertEqual(
            dict(**result),
            dict(first_name=name, last_name=surname),
        )
