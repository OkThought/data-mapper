from unittest import TestCase

from data_mapper.properties import StringProperty, CompoundProperty
from data_mapper.shortcuts import V, P, F, R


class ShortcutsTests(TestCase):
    def _test(self, expected, prop, data=None):
        if data is None:
            data = {}
        self.assertEqual(expected, prop.get(data))

    def test__v(self):
        self._test(1, V(1))

    def test__v__lt(self):
        self._test(True, V(3) < V(5))
        self._test(False, V(5) < V(3))

    def test__v__le(self):
        self._test(True, V(3) <= V(3))
        self._test(False, V(3) <= V(2))

    def test__v__eq(self):
        self._test(False, V(3) == V(1))
        self._test(True, V(3) == V(3))

    def test__v__ne(self):
        self._test(True, V(3) != V(2))
        self._test(False, V(2) != V(2))

    def test__v__ge(self):
        self._test(True, V(5) >= V(5))
        self._test(True, V(6) >= V(5))
        self._test(False, V(4) >= V(5))

    def test__v__gt(self):
        self._test(True, V(5) > V(4))
        self._test(False, V(4) > V(4))
        self._test(False, V(3) > V(4))

    def test__v__abs(self):
        self._test(1, abs(V(-1)))
        self._test(1, abs(V(+1)))

    def test__v__and(self):
        self._test(True, V(True) & V(True))
        self._test(False, V(True) & V(False))
        self._test(False, V(False) & V(True))
        self._test(False, V(False) & V(False))
        self._test(True, V(True) & True)
        self._test(False, V(True) & False)
        self._test(False, V(False) & True)
        self._test(False, V(False) & False)

    def test__v__or(self):
        self._test(True, V(True) | V(True))
        self._test(True, V(True) | V(False))
        self._test(True, V(False) | V(True))
        self._test(False, V(False) | V(False))
        self._test(True, V(True) | True)
        self._test(True, V(True) | False)
        self._test(True, V(False) | True)
        self._test(False, V(False) | False)

    def test__v__neg(self):
        self._test(-1, -V(1))
        self._test(1, -V(-1))

    def test__v__pos(self):
        self._test(+1, +V(1))

    def test__v__add(self):
        self._test(2, V(1) + V(1))
        self._test(3, V(1) + V(2))
        self._test(0, V(1) + V(-1))

    def test__v__floordiv(self):
        self._test(0, V(1) // V(2))
        self._test(1, V(2) // V(2))
        self._test(1, V(3) // 2)

    def test__v__mod(self):
        self._test(1, V(5) % V(2))
        self._test(1, V(5) % 2)

    def test__v__mul(self):
        self._test(4, V(2) * V(2))
        self._test(6, V(2) * 3)

    def test__v__matmul(self):
        pass

    def test__v__pow(self):
        self._test(4, V(2) ** V(2))
        self._test(4, V(2) ** 2)

    def test__v__sub(self):
        self._test(-1, V(1) - V(2))
        self._test(-1, V(1) - 2)

    def test__v__truediv(self):
        self._test(2.5, V(5) / V(2))
        self._test(2.5, V(5) / 2)

    def test__v__invert(self):
        self._test(~5, ~V(5))
        self._test(~1, ~V(1))
        self._test(~0, ~V(0))
        self._test(~-1, ~V(-1))
        self._test(~-9, ~V(-9))

    def test__v__lshift(self):
        self._test(25 << 2, V(25) << V(2))
        self._test(25 << 2, V(25) << 2)

    def test__v__rshift(self):
        self._test(25 >> 2, V(25) >> V(2))
        self._test(25 >> 2, V(25) >> 2)

    def test__v__xor(self):
        self._test(7 ^ 3, V(7) ^ V(3))
        self._test(7 ^ 3, V(7) ^ 3)

    def test__v__getitem__dict(self):
        self._test(5, V({'x': 5})[V('x')])
        self._test(5, V({'x': 5})['x'])

    def test__v__getitem__str(self):
        self._test('3', V('0123')[V(3)])
        self._test('3', V('0123')[3])

    def test__v__getitem__list(self):
        self._test(2, V(list(range(3)))[-1])
        self._test(0, V(list(range(3)))[V(0)])
        self._test(1, V(list(range(3)))[1])
        self._test(2, V(list(range(3)))[2])

    def test__v__delitem__dict(self):
        self._test({'x': 5}, V({'x': 5, 'y': 6}).delitem(V('y')))
        self._test({'y': 6}, V({'x': 5, 'y': 6}).delitem('x'))

    def test__v__delitem__list(self):
        self._test([1], V([1, 2]).delitem(V(1)))
        self._test([1], V([1, 2]).delitem(-1))
        self._test([2], V([1, 2]).delitem(0))

    def test__v__setitem__dict(self):
        self._test({'x': 5}, V({}).set(V('x'), V(5)))
        self._test({'x': 5}, V({}).set(V('x'), 5))
        self._test({'x': 5}, V({}).set('x', V(5)))
        self._test({'x': 5}, V({}).set('x', 5))

    def test__v__setitem__list(self):
        self._test([1, 3], V([1, 2]).set(V(1), V(3)))
        self._test([1, 3], V([1, 2]).set(1, V(3)))
        self._test([1, 3], V([1, 2]).set(V(1), 3))
        self._test([1, 3], V([1, 2]).set(1, 3))
        self._test([1, 3], V([1, 2]).set(-1, 3))

    def test__v__concat(self):
        self._test([1, 2], V([1]).concat(V([2])))
        self._test([1, 2], V([1]).concat([2]))

    def test__v__contains(self):
        self._test(True, V({1, 2}).contains(V(1)))
        self._test(True, V({1, 2}).contains(2))
        self._test(False, V({1, 2}).contains(3))

    def test__v__count_of(self):
        self._test(0, V(list([2, 1, 2])).count_of(V(0)))
        self._test(1, V(list([2, 1, 2])).count_of(V(1)))
        self._test(2, V(list([2, 1, 2])).count_of(V(2)))
        self._test(0, V(list([2, 1, 2])).count_of(V(3)))
        self._test(0, V(list([2, 1, 2])).count_of(0))
        self._test(1, V(list([2, 1, 2])).count_of(1))
        self._test(2, V(list([2, 1, 2])).count_of(2))
        self._test(0, V(list([2, 1, 2])).count_of(3))

    def test__v__index_of(self):
        self._test(0, V(list([2, 1, 2])).index_of(V(2)))
        self._test(1, V(list([2, 1, 2])).index_of(V(1)))
        with self.assertRaises(ValueError):
            self._test(None, V(list([2, 1, 2])).index_of(V(0)))
        self._test(0, V(list([2, 1, 2])).index_of(2))
        self._test(1, V(list([2, 1, 2])).index_of(1))

    def test__p(self):
        self._test(1, P(0), [1])
        self._test(2, P(1), [1, 2])
        self._test(3, P(1), {1: 3})

    def test__f(self):
        full_name = 'Ayn Rand'
        name, surname = full_name.split()

        self._test(
            full_name,
            F(' '.join, args=[V([name, surname])]),
        )
        self._test(
            [name, surname],
            F(str.split, args=[V(full_name)]),
        )

    def test__r(self):

        self._test(
            dict(days=1, hours=1, minutes=30, total_hours=25.5),
            CompoundProperty(
                total_hours=R('days') * 24 + R('hours') + R('minutes') / 60,
                days=V(1),
                hours=V(1),
                minutes=V(30),
            ),
        )
