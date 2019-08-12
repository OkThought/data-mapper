from unittest import TestCase

from data_mapper.properties.value import Value, V


class ValueTests(TestCase):
    def test(self):
        self.assertEqual('a', Value('a').get({}))
        self.assertEqual(1, Value(1).get({}))

    def test__shortcut(self):
        self.assertEqual('a', V('a').get({}))
