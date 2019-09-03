from data_mapper.errors import ValidationError
from data_mapper.properties.list import ListProperty
from data_mapper.tests.test_utils import PropertyTests


class ListPropertyTests(PropertyTests):
    def test__empty(self):
        self.prop_test(ListProperty(['x']), [], dict(x=[]))

    def test__nonempty(self):
        self.prop_test(ListProperty(['x']), [1], dict(x=[1]))

    def test__many_sources(self):
        self.prop_test(
            ListProperty('x', 'y', 'z'),
            [1., '2'],
            dict(y=[1., '2'], z=[3]),
        )

    def test__range(self):
        self.prop_test(ListProperty('x'), [0, 1, 2], dict(x=range(3)))

    def test__transforms__filter_positive(self):
        positive = ListProperty(
            ['numbers'],
            transforms=[
                lambda l: [i for i in l if i > 0],
            ],
        )
        self.assertEqual(positive.get(dict(numbers=[-1, 0, 1])), [1])

    def test__validate__only_floats(self):
        prop = ListProperty('x', allowed_types=(float,))
        with self.assertRaises(ValidationError):
            prop.get(dict(x=[1., 2., '3']))

        with self.assertRaises(ValidationError):
            prop.get(dict(x=[1., 2., 3]))

        prop.get(dict(x=[1., 2., 3.]))

    def test__none(self):
        self.prop_test(
            prop=ListProperty('x', required=False),
            data=dict(x=None),
            expect=None,
        )
        self.prop_test(
            prop=ListProperty('x', required=False),
            data=dict(),
            expect=None,
        )
