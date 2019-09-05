from data_mapper.properties import CompoundProperty
from data_mapper.shortcuts import (
    V, P, F, R, D, Op, Bool, Str, Int, Float,
    Dict, List,
    L,
)
from data_mapper.tests.test_utils import PropertyTests


class ShortcutsTests(PropertyTests):
    def test__v(self):
        self.prop_test(V(1), 1)

    def test__v__lt(self):
        self.prop_test(V(3) < V(5), True)
        self.prop_test(V(5) < V(3), False)

    def test__v__le(self):
        self.prop_test(V(3) <= V(3), True)
        self.prop_test(V(3) <= V(2), False)

    def test__v__eq(self):
        self.prop_test(V(3) == V(1), False)
        self.prop_test(V(3) == V(3), True)

    def test__v__ne(self):
        self.prop_test(V(3) != V(2), True)
        self.prop_test(V(2) != V(2), False)

    def test__v__ge(self):
        self.prop_test(V(5) >= V(5), True)
        self.prop_test(V(6) >= V(5), True)
        self.prop_test(V(4) >= V(5), False)

    def test__v__gt(self):
        self.prop_test(V(5) > V(4), True)
        self.prop_test(V(4) > V(4), False)
        self.prop_test(V(3) > V(4), False)

    def test__v__abs(self):
        self.prop_test(abs(V(-1)), 1)
        self.prop_test(abs(V(+1)), 1)

    def test__v__and(self):
        self.prop_test(V(True) & V(True), True)
        self.prop_test(V(True) & V(False), False)
        self.prop_test(V(False) & V(True), False)
        self.prop_test(V(False) & V(False), False)
        self.prop_test(V(True) & True, True)
        self.prop_test(V(True) & False, False)
        self.prop_test(V(False) & True, False)
        self.prop_test(V(False) & False, False)

    def test__v__or(self):
        self.prop_test(V(True) | V(True), True)
        self.prop_test(V(True) | V(False), True)
        self.prop_test(V(False) | V(True), True)
        self.prop_test(V(False) | V(False), False)
        self.prop_test(V(True) | True, True)
        self.prop_test(V(True) | False, True)
        self.prop_test(V(False) | True, True)
        self.prop_test(V(False) | False, False)

    def test__v__neg(self):
        self.prop_test(-V(1), -1)
        self.prop_test(-V(-1), 1)

    def test__v__pos(self):
        self.prop_test(+V(1), +1)

    def test__v__add(self):
        self.prop_test(V(1) + V(1), 2)
        self.prop_test(V(1) + V(2), 3)
        self.prop_test(V(1) + V(-1), 0)

    def test__v__floordiv(self):
        self.prop_test(V(1) // V(2), 0)
        self.prop_test(V(2) // V(2), 1)
        self.prop_test(V(3) // 2, 1)

    def test__v__mod(self):
        self.prop_test(V(5) % V(2), 1)
        self.prop_test(V(5) % 2, 1)

    def test__v__mul(self):
        self.prop_test(V(2) * V(2), 4)
        self.prop_test(V(2) * 3, 6)

    def test__v__matmul(self):
        pass

    def test__v__pow(self):
        self.prop_test(V(2) ** V(2), 4)
        self.prop_test(V(2) ** 2, 4)

    def test__v__sub(self):
        self.prop_test(V(1) - V(2), -1)
        self.prop_test(V(1) - 2, -1)

    def test__v__truediv(self):
        self.prop_test(V(5) / V(2), 2.5)
        self.prop_test(V(5) / 2, 2.5)

    def test__v__invert(self):
        self.prop_test(~V(5), ~5)
        self.prop_test(~V(1), ~1)
        self.prop_test(~V(0), ~0)
        self.prop_test(~V(-1), ~-1)
        self.prop_test(~V(-9), ~-9)

    def test__v__lshift(self):
        self.prop_test(V(25) << V(2), 25 << 2)
        self.prop_test(V(25) << 2, 25 << 2)

    def test__v__rshift(self):
        self.prop_test(V(25) >> V(2), 25 >> 2)
        self.prop_test(V(25) >> 2, 25 >> 2)

    def test__v__xor(self):
        self.prop_test(V(7) ^ V(3), 7 ^ 3)
        self.prop_test(V(7) ^ 3, 7 ^ 3)

    def test__v__getitem__dict(self):
        self.prop_test(V({'x': 5})[V('x')], 5)
        self.prop_test(V({'x': 5})['x'], 5)

    def test__v__getitem__str(self):
        self.prop_test(V('0123')[V(3)], '3')
        self.prop_test(V('0123')[3], '3')

    def test__v__getitem__list(self):
        self.prop_test(V(list(range(3)))[-1], 2)
        self.prop_test(V(list(range(3)))[V(0)], 0)
        self.prop_test(V(list(range(3)))[1], 1)
        self.prop_test(V(list(range(3)))[2], 2)

    def test__v__delitem__dict(self):
        self.prop_test(V({'x': 5, 'y': 6}).delitem(V('y')), {'x': 5})
        self.prop_test(V({'x': 5, 'y': 6}).delitem('x'), {'y': 6})

    def test__v__delitem__list(self):
        self.prop_test(V([1, 2]).delitem(V(1)), [1])
        self.prop_test(V([1, 2]).delitem(-1), [1])
        self.prop_test(V([1, 2]).delitem(0), [2])

    def test__v__setitem__dict(self):
        self.prop_test(V({}).set(V('x'), V(5)), {'x': 5})
        self.prop_test(V({}).set(V('x'), 5), {'x': 5})
        self.prop_test(V({}).set('x', V(5)), {'x': 5})
        self.prop_test(V({}).set('x', 5), {'x': 5})

    def test__v__setitem__list(self):
        self.prop_test(V([1, 2]).set(V(1), V(3)), [1, 3])
        self.prop_test(V([1, 2]).set(1, V(3)), [1, 3])
        self.prop_test(V([1, 2]).set(V(1), 3), [1, 3])
        self.prop_test(V([1, 2]).set(1, 3), [1, 3])
        self.prop_test(V([1, 2]).set(-1, 3), [1, 3])

    def test__v__concat(self):
        self.prop_test(V([1]).concat(V([2])), [1, 2])
        self.prop_test(V([1]).concat([2]), [1, 2])

    def test__v__contains(self):
        self.prop_test(V({1, 2}).contains(V(1)), True)
        self.prop_test(V({1, 2}).contains(2), True)
        self.prop_test(V({1, 2}).contains(3), False)

    def test__v__count_of(self):
        self.prop_test(V(list([2, 1, 2])).count_of(V(0)), 0)
        self.prop_test(V(list([2, 1, 2])).count_of(V(1)), 1)
        self.prop_test(V(list([2, 1, 2])).count_of(V(2)), 2)
        self.prop_test(V(list([2, 1, 2])).count_of(V(3)), 0)
        self.prop_test(V(list([2, 1, 2])).count_of(0), 0)
        self.prop_test(V(list([2, 1, 2])).count_of(1), 1)
        self.prop_test(V(list([2, 1, 2])).count_of(2), 2)
        self.prop_test(V(list([2, 1, 2])).count_of(3), 0)

    def test__v__index_of(self):
        self.prop_test(V(list([2, 1, 2])).index_of(V(2)), 0)
        self.prop_test(V(list([2, 1, 2])).index_of(V(1)), 1)
        with self.assertRaises(ValueError):
            self.prop_test(V(list([2, 1, 2])).index_of(V(0)), None)
        self.prop_test(V(list([2, 1, 2])).index_of(2), 0)
        self.prop_test(V(list([2, 1, 2])).index_of(1), 1)

    def test__p(self):
        self.prop_test(P(0), 1, [1])
        self.prop_test(P(1), 2, [1, 2])
        self.prop_test(P(1), 3, {1: 3})

    def test__f(self):
        full_name = 'Ayn Rand'
        name, surname = full_name.split()

        self.prop_test(
            F(' '.join, args=[V([name, surname])]),
            full_name,
        )
        self.prop_test(
            F(str.split, args=[V(full_name)]),
            [name, surname],
        )

    def test__r(self):

        self.prop_test(
            CompoundProperty(
                total_hours=R('days') * 24 + R('hours') + R('minutes') / 60,
                days=V(1),
                hours=V(1),
                minutes=V(30),
            ),
            dict(days=1, hours=1, minutes=30, total_hours=25.5),
        )

    def test__op(self):
        self.prop_test(Op(V(3), V(2), star_func=lambda x, y: x ** y), 9)

    def test__bool(self):
        self.prop_test(Bool(V(False)), False)

    def test__str(self):
        self.prop_test(Str(V(1)), '1')

    def test__int(self):
        self.prop_test(Int(V('1')), 1)

    def test__float(self):
        self.prop_test(Float(V('1.1')), 1.1)

    def test__dict(self):
        self.prop_test(Dict(V(dict(x=1, y=2))), dict(x=1, y=2))

    def test__list(self):
        self.prop_test(List(V((1, 2, 3))), [1, 2, 3])

    def test__d(self):
        self.prop_test(D(x=V(1)), dict(x=1))

    def test__l(self):
        self.prop_test(L(V(1), V(2)), [1, 2])
