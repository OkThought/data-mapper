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

    def test__invalid_data(self):
        self.prop_not_found(ListProperty(0), data=[1])
        self.prop_not_found(ListProperty(0), data=[1])

    def test__invalid_data__followed_by_valid(self):
        self.prop_test(ListProperty(0, 1), [2], [1, [2]])

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
