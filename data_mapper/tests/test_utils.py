from unittest import TestCase

from data_mapper.errors import PropertyNotResolved


class Person:
    def __init__(
            self,
            id_: int,
            first_name: str,
            last_name: str,
            middle_name: str = None,
    ):
        self.id = id_
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name

    def __eq__(self, other):
        return (
                isinstance(other, Person) and
                self.id == other.id and
                self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.middle_name == other.middle_name
        )

    def __repr__(self):
        return f'{self.__class__.__name__}(' \
               f'{self.id}, {self.first_name}, {self.last_name}, ' \
               f'{self.middle_name})'


class PropertyTestCase(TestCase):
    def prop_test(
            self,
            prop,
            expect=None,
            data=None,
            exc=None,
            result=None
    ):
        if data is None:
            data = {}
        if exc is not None:
            with self.assertRaises(exc):
                prop.get(data, result=result)
        else:
            self.assertEqual(expect, prop.get(data, result=result))

    def prop_raises(
            self,
            exc,
            prop,
            data=None,
    ):
        self.prop_test(prop, data=data, exc=exc)

    def prop_not_found(self, prop, data=None):
        self.prop_raises(PropertyNotResolved, prop, data)
