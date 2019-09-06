from data_mapper.errors import PropertyNotResolved
from data_mapper.properties.integer import IntegerProperty
from data_mapper.properties.property import Property
from data_mapper.properties.string import StringProperty
from data_mapper.properties.value import Value
from data_mapper.tests.test_utils import Person, PropertyTests


# noinspection PyRedeclaration
class PropertyTests(PropertyTests):
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

    def test__sources_it(self):
        with self.assertRaises(AssertionError):
            Property('x', sources_it=('x',))
        prop = Property(sources_it=range(6))
        self.assertEqual(3, prop.get({i: i for i in range(3, 6)}))
        self.assertEqual(2, prop.get({i: i for i in range(2, 6)}))
        self.assertEqual(1, prop.get({i: i for i in range(1, 6)}))
        self.assertEqual(0, prop.get({i: i for i in range(0, 6)}))

    def test__sources__property(self):
        self.assertEqual(1, Property(Value(1)).get({}))

    def test__sources__property__not_found(self):
        with self.assertRaises(PropertyNotResolved):
            Property(Property('x')).get({})

    def test__sources__properties(self):
        self.assertEqual(1, Property(Property('x'), Value(1)).get({}))

    def test__sources__properties__nested(self):
        self.assertEqual(1, Property([Value(dict(x=1)), Property('x')]).get({}))

    def test__get_value__from_object(self):
        first, middle, last = 'Alexander Sergeyevich Pushkin'.split()
        pushkin = Person(1799, first, last, middle)

        prop = IntegerProperty(
            'id', get_value=getattr, get_value_exc=AttributeError)
        self.assertEqual(1799, prop.get(pushkin))

        prop = StringProperty(
            'first_name', get_value=getattr, get_value_exc=AttributeError)
        self.assertEqual(first, prop.get(pushkin))

        prop = StringProperty(
            'middle_name', get_value=getattr, get_value_exc=AttributeError)
        self.assertEqual(middle, prop.get(pushkin))

        prop = StringProperty(
            'last_name', get_value=getattr, get_value_exc=AttributeError)
        self.assertEqual(last, prop.get(pushkin))

        prop = StringProperty(
            'unknown', get_value=getattr, get_value_exc=AttributeError)
        with self.assertRaises(PropertyNotResolved):
            prop.get(pushkin)
