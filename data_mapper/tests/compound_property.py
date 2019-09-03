from data_mapper.properties import Property
from data_mapper.properties.compound import CompoundProperty
from data_mapper.properties.string import StringProperty
from data_mapper.tests.test_utils import PropertyTests


class CompoundPropertyTests(PropertyTests):
    def test(self):
        prop = CompoundProperty(
            first_name=StringProperty(['name']),
            last_name=StringProperty(['surname']),
        )
        name, surname = 'Pauline Gvozd'.split()
        self.assertEqual(
            dict(first_name=name, last_name=surname),
            prop.get(data=dict(name=name, surname=surname)),
        )

    def test__not_lazy(self):
        prop = CompoundProperty(
            first_name=StringProperty(['name']),
            last_name=StringProperty(['surname']),
            _options=dict(lazy=False),
        )
        name, surname = 'Pauline Gvozd'.split()
        self.assertEqual(
            dict(first_name=name, last_name=surname),
            prop.get(data=dict(name=name, surname=surname)),
        )

    def test__properties_no_sources(self):
        prop = CompoundProperty(
            first_name=StringProperty(),
            last_name=StringProperty(),
        )
        first_name, last_name = 'Pauline Gvozd'.split()
        self.assertEqual(
            dict(first_name=first_name, last_name=last_name),
            prop.get(data=dict(first_name=first_name, last_name=last_name)),
        )

    def test__get_value__set_in_parent(self):
        prop = CompoundProperty(
            dict(get_value=lambda *_: 'foo'),
            x=Property(),
        )
        self.assertEqual('foo', prop.get(dict(x=5))['x'])

    def test__get_value__set_in_grand_parent(self):
        prop = CompoundProperty(
            dict(get_value=lambda *_: 'foo'),
            y=CompoundProperty(
                x=Property(),
            ),
        )
        self.assertEqual('foo', prop.get(dict(x=5))['y']['x'])
