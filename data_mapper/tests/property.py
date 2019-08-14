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

    def test__default(self):
        self.assertEqual(1, Property('x', default=1).get({}))

    def test__default_none(self):
        self.assertEqual(None, Property('x', default=None).get({}))

    def test__default_required(self):
        with self.assertRaises(AssertionError):
            Property(default=5, required=True)
        with self.assertRaises(AssertionError):
            Property(default=None, required=True)
        with self.assertRaises(AssertionError):
            Property(default=0, required=True)

    def test__add(self):
        prop = Property('x') + Property('y')
        self.assertEqual(3, prop.get(dict(x=1, y=2)))

    def test__sub(self):
        prop = Property('x') - Property('y')
        self.assertEqual(-1, prop.get(dict(x=1, y=2)))

    def test__mul(self):
        prop = Property('x') * Property('y')
        self.assertEqual(4, prop.get(dict(x=2, y=2)))

    def test__div(self):
        prop = Property('x') / Property('y')
        self.assertEqual(2.5, prop.get(dict(x=5, y=2)))
