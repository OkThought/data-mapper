from unittest import TestCase

from src.properties.compound import CompoundProperty
from src.properties.string import StringProperty


class CompoundPropertyTests(TestCase):
    def test__dict(self):
        prop = CompoundProperty(dict(
            first_name=StringProperty(['name']),
            last_name=StringProperty(['surname']),
        ))
        name, surname = 'Pauline Gvozd'.split()
        self.assertEqual(
            dict(first_name=name, last_name=surname),
            dict(prop.get(data=dict(name=name, surname=surname))),
        )
