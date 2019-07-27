from unittest import TestCase

from src.properties.list import ListProperty


class ListPropertyTests(TestCase):
    def test__empty(self):
        prop = ListProperty(sources=['x'])
        self.assertEqual(prop.get(dict(x=[])), [])

    def test__nonempty(self):
        prop = ListProperty(sources=['x'])
        self.assertEqual(prop.get(dict(x=[1])), [1])

    def test__many_sources(self):
        prop = ListProperty(sources='xyz')
        self.assertEqual(prop.get(dict(y=[1., '2'], z=[3])), [1., '2'])

    def test__range(self):
        prop = ListProperty(sources='x')
        self.assertEqual(prop.get(dict(x=range(3))), [0, 1, 2])

    def test__transforms__filter_positive(self):
        positive = ListProperty(
            sources=['numbers'],
            transforms=[
                lambda l: [i for i in l if i > 0],
            ],
        )
        self.assertEqual(positive.get(dict(numbers=[-1, 0, 1])), [1])
