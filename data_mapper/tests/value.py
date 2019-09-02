from unittest import TestCase

from data_mapper.properties.value import Value


class ValueTests(TestCase):
    def test(self):
        self.assertEqual('a', Value('a').get({}))
        self.assertEqual(1, Value(1).get({}))
