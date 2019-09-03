from unittest import TestCase

from data_mapper.properties import Property
from data_mapper.properties.functional.operation import Operation
from data_mapper.properties.string import StringProperty


class PropertyOperationTests(TestCase):
    def test__count_not_none(self):
        def count_not_none(args):
            return sum(1 for a in args if a is not None)

        prop = Operation(func=count_not_none)
        self.assertEqual(0, prop.get({}))

        prop = Operation(prop, func=count_not_none)
        self.assertEqual(1, prop.get({}))

        name = StringProperty('name', 'first_name', default=None)
        surname = StringProperty('surname', 'family_name', default=None)
        prop = Operation(name, surname, func=count_not_none)
        self.assertEqual(0, prop.get({}))

    def test__date_format(self):
        prop = Operation(
            StringProperty('year', default='2019'),
            StringProperty('month'),
            StringProperty('day'),
            func='.'.join,
        )
        data = {'month': 8, 'day': 12}
        self.assertEqual('2019.8.12', prop.get(data))

    def test__get_value__set_in_parent(self):
        prop = Operation(
            Property('x'),
            star_func=lambda x: x,
            get_value=lambda *_: 'foo',
        )
        self.assertEqual('foo', prop.get(dict(x=5)))

    def test__get_value__set_in_grand_parent(self):
        prop = Operation(
            Operation(Property('x'), star_func=lambda x: x),
            star_func=lambda x: x,
            get_value=lambda *_: 'foo',
        )
        self.assertEqual('foo', prop.get(dict(x=5)))
