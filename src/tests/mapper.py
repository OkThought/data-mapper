from unittest import TestCase

from src.mappers.mapper import Mapper


class MapperTests(TestCase):
    def test__properties__get_absent(self):
        mapper = Mapper()
        result = mapper.get(dict(a=1))
        with self.assertRaises(KeyError):
            # noinspection PyStatementEffect
            result['a']
