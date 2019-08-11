from unittest import TestCase

from data_mapper.properties.compound import CompoundProperty
from data_mapper.properties.string import StringProperty


class CompoundPropertyTests(TestCase):
    def test__dict(self):
        prop = CompoundProperty((), props_map=dict(
            first_name=StringProperty(['name']),
            last_name=StringProperty(['surname']),
        ))
        name, surname = 'Pauline Gvozd'.split()
        self.assertEqual(
            dict(first_name=name, last_name=surname),
            dict(prop.get(data=dict(name=name, surname=surname))),
        )
