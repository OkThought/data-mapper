from unittest import TestCase

from data_mapper.properties.property import Property
from data_mapper.properties.string import StringProperty


class PropertyTests(TestCase):
    def test__root_source(self):
        prop = Property([])
        data = dict(x=1)
        self.assertEqual(data, prop.get(data))
        prop = Property('y', [], 'x')
        self.assertEqual(data, prop.get(data))

    def test__no_sources(self):
        prop = Property()
        data = dict(x=1)
        self.assertEqual(data, prop.get(data))

    def test__str(self):
        self.assertEqual('Property<[]>', str(Property([])))
        self.assertEqual("Property<'x'>", str(Property('x')))
        self.assertEqual("Property<'x','y'>", str(Property('x', 'y')))
        self.assertEqual('StringProperty<None>', str(StringProperty()))
