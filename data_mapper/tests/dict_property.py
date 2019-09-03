from data_mapper.properties.dict import DictProperty
from data_mapper.tests.test_utils import PropertyTests


class DictPropertyTests(PropertyTests):
    def test__dict(self):
        address = dict(
            city='London',
            street='Baker Street',
            property_number='221B',
        )
        self.prop_test(
            prop=DictProperty(['address']),
            data=dict(address=address),
            expect=address
        )

    def test__key_value_pairs(self):
        address = dict(
            city='London',
            street='Baker Street',
            property_number='221B',
        )
        self.prop_test(
            prop=DictProperty(['address']),
            data=dict(address=list(address.items())),
            expect=address
        )
