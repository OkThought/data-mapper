from unittest import TestCase

from data_mapper.mappers.mapper import Mapper
from data_mapper.properties import Value
from data_mapper.properties.compound import CompoundProperty
from data_mapper.properties.ref import PropertyRef
from data_mapper.properties.string import StringProperty


class PropertyRefTests(TestCase):
    def test__empty_source(self):
        with self.assertRaises(AssertionError):
            PropertyRef().get({})
        with self.assertRaises(AssertionError):
            PropertyRef(sources_it=[]).get({})

    def test__flat_source(self):
        class MyMapper(Mapper):
            first_name = StringProperty('name')
            also_first_name = PropertyRef('first_name')
        mapper = MyMapper()
        name = 'Leo'
        result = mapper.get(dict(name=name))
        self.assertEqual(name, result['first_name'])
        self.assertEqual(name, result['also_first_name'])

    def test__deep_source(self):
        class MyMapper(Mapper):
            full_name = CompoundProperty(
                first_name=StringProperty('name'),
                last_name=StringProperty('surname'),
            )
            first_name = PropertyRef('full_name', 'first_name')
        mapper = MyMapper()
        name, surname = 'Peter Pan'.split()
        result = mapper.get(dict(name=name, surname=surname))
        self.assertEqual(name, result['first_name'])

    def test__deep(self):
        class MyMapper(Mapper):
            full_name = CompoundProperty(
                first_name=StringProperty('name'),
                last_name=PropertyRef('last_name'),
            )
            last_name = Value('Pan')
        mapper = MyMapper()
        name, surname = 'Peter Pan'.split()
        result = mapper.get(dict(name=name))
        self.assertEqual(
            dict(
                full_name=dict(
                    first_name=name,
                    last_name=surname,
                ),
                last_name=surname,
            ),
            result,
        )

    def test__flat_source__bc(self):
        class MyMapper(Mapper):
            first_name = StringProperty(['name'])
            also_first_name = PropertyRef(['first_name'])

        mapper = MyMapper()
        name = 'Leo'
        result = mapper.get(dict(name=name))
        self.assertEqual(name, result['first_name'])
        self.assertEqual(name, result['also_first_name'])

    def test__deep_source__bc(self):
        class MyMapper(Mapper):
            full_name = CompoundProperty(
                first_name=StringProperty(['name']),
                last_name=StringProperty(['surname']),
            )
            first_name = PropertyRef(['full_name', 'first_name'])

        mapper = MyMapper()
        name, surname = 'Peter Pan'.split()
        result = mapper.get(dict(name=name, surname=surname))
        self.assertEqual(name, result['first_name'])

    def test__deep__bc(self):
        class MyMapper(Mapper):
            full_name = CompoundProperty(
                first_name=StringProperty('name'),
                last_name=PropertyRef(['last_name']),
            )
            last_name = Value('Pan')

        mapper = MyMapper()
        name, surname = 'Peter Pan'.split()
        result = mapper.get(dict(name=name))
        self.assertEqual(
            dict(
                full_name=dict(
                    first_name=name,
                    last_name=surname,
                ),
                last_name=surname,
            ),
            result,
        )
