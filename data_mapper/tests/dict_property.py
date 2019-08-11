from unittest import TestCase

from data_mapper.properties.dict import DictProperty


class DictPropertyTests(TestCase):
    def _test(self, prop, data, expected):
        result = prop.get(data)
        self.assertEqual(expected, result)

    def test__dict(self):
        address = dict(
            city='London',
            street='Baker Street',
            property_number='221B',
        )
        self._test(
            prop=DictProperty(['address']),
            data=dict(address=address),
            expected=address
        )

    def test__key_value_pairs(self):
        address = dict(
            city='London',
            street='Baker Street',
            property_number='221B',
        )
        self._test(
            prop=DictProperty(['address']),
            data=dict(address=list(address.items())),
            expected=address
        )
