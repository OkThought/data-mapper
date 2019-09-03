from abc import ABC

from data_mapper.properties.abstract import AbstractProperty


__all__ = [
    'ComparisonOperations',
    'LogicalUnaryOperations',
    'LogicalBinaryOperations',
    'MathUnaryOperations',
    'MathBinaryOperations',
    'BitwiseUnaryOperations',
    'BitwiseBinaryOperations',
    'SequenceBinaryOperations',
    'SequenceTernaryOperations',
    'SequenceOperations',
    'MathOperations',
    'LogicalOperations',
    'BitwiseOperations',
    'AllOperations',
]


def _make_prop(obj):
    if not isinstance(obj, AbstractProperty):
        from data_mapper.properties import Value
        obj = Value(obj)
    return obj


class ComparisonOperations(AbstractProperty, ABC):
    def __lt__(self, other):
        from data_mapper.properties.functional.operators import Lt
        return Lt(self, _make_prop(other))

    def __le__(self, other):
        from data_mapper.properties.functional.operators import Le
        return Le(self, _make_prop(other))

    def __eq__(self, other):
        from data_mapper.properties.functional.operators import Eq
        return Eq(self, _make_prop(other))

    def __ne__(self, other):
        from data_mapper.properties.functional.operators import Ne
        return Ne(self, _make_prop(other))

    def __ge__(self, other):
        from data_mapper.properties.functional.operators import Ge
        return Ge(self, _make_prop(other))

    def __gt__(self, other):
        from data_mapper.properties.functional.operators import Gt
        return Gt(self, _make_prop(other))


class LogicalUnaryOperations(AbstractProperty, ABC):
    def __not__(self):
        from data_mapper.properties.functional.operators import Not
        return Not(self)

    def truth(self):
        from data_mapper.properties.functional.operators import Truth
        return Truth(self)


class LogicalBinaryOperations(AbstractProperty, ABC):
    def is_(self, other):
        from data_mapper.properties.functional.operators import Is
        return Is(self, _make_prop(other))

    def is_not(self, other):
        from data_mapper.properties.functional.operators import IsNot
        return IsNot(self, _make_prop(other))


class MathUnaryOperations(AbstractProperty, ABC):
    def __abs__(self):
        from data_mapper.properties.functional.operators import Abs
        return Abs(self)

    def __index__(self):
        from data_mapper.properties.functional.operators import Index
        return Index(self)

    def __neg__(self):
        from data_mapper.properties.functional.operators import Neg
        return Neg(self)

    def __pos__(self):
        from data_mapper.properties.functional.operators import Pos
        return Pos(self)


class MathBinaryOperations(AbstractProperty, ABC):
    def __add__(self, other):
        from data_mapper.properties.functional.operators import Add
        return Add(self, _make_prop(other))

    def __floordiv__(self, other):
        from data_mapper.properties.functional.operators import Floordiv
        return Floordiv(self, _make_prop(other))

    def __mod__(self, other):
        from data_mapper.properties.functional.operators import Mod
        return Mod(self, _make_prop(other))

    def __mul__(self, other):
        from data_mapper.properties.functional.operators import Mul
        return Mul(self, _make_prop(other))

    def __matmul__(self, other):
        from data_mapper.properties.functional.operators import Matmul
        return Matmul(self, _make_prop(other))

    def __pow__(self, other):
        from data_mapper.properties.functional.operators import Pow
        return Pow(self, _make_prop(other))

    def __sub__(self, other):
        from data_mapper.properties.functional.operators import Sub
        return Sub(self, _make_prop(other))

    def __truediv__(self, other):
        from data_mapper.properties.functional.operators import Truediv
        return Truediv(self, _make_prop(other))


class BitwiseUnaryOperations(AbstractProperty, ABC):
    def __invert__(self):
        from data_mapper.properties.functional.operators import Inv
        return Inv(self)


class BitwiseBinaryOperations(AbstractProperty, ABC):
    def __and__(self, other):
        from data_mapper.properties.functional.operators import And
        return And(self, _make_prop(other))

    def __lshift__(self, other):
        from data_mapper.properties.functional.operators import Lshift
        return Lshift(self, _make_prop(other))

    def __or__(self, other):
        from data_mapper.properties.functional.operators import Or
        return Or(self, _make_prop(other))

    def __rshift__(self, other):
        from data_mapper.properties.functional.operators import Rshift
        return Rshift(self, _make_prop(other))

    def __xor__(self, other):
        from data_mapper.properties.functional.operators import Xor
        return Xor(self, _make_prop(other))


class SequenceBinaryOperations(AbstractProperty, ABC):
    def concat(self, other):
        from data_mapper.properties.functional.operators import Concat
        return Concat(self, _make_prop(other))

    def contains(self, other):
        from data_mapper.properties.functional.operators import Contains
        return Contains(self, _make_prop(other))

    def count_of(self, other):
        from data_mapper.properties.functional.operators import CountOf
        return CountOf(self, _make_prop(other))

    def delitem(self, other):
        from data_mapper.properties.functional.operators import Delitem
        return Delitem(self, _make_prop(other))

    def index_of(self, other):
        from data_mapper.properties.functional.operators import IndexOf
        return IndexOf(self, _make_prop(other))

    def __getitem__(self, key):
        from data_mapper.properties.functional.operators import Getitem
        return Getitem(self, _make_prop(key))


class SequenceTernaryOperations(AbstractProperty, ABC):
    def set(self, key, val):
        from data_mapper.properties.functional.operators import Setitem
        return Setitem(self, _make_prop(key), _make_prop(val))


class SequenceOperations(
    SequenceBinaryOperations,
    SequenceTernaryOperations,
    ABC,
):
    pass


class MathOperations(
    MathUnaryOperations,
    MathBinaryOperations,
    ABC,
):
    pass


class LogicalOperations(
    LogicalUnaryOperations,
    LogicalBinaryOperations,
    ABC,
):
    pass


class BitwiseOperations(
    BitwiseUnaryOperations,
    BitwiseBinaryOperations,
    ABC,
):
    pass


class AllOperations(
    ComparisonOperations,
    LogicalOperations,
    MathOperations,
    BitwiseOperations,
    SequenceOperations,
    ABC,
):
    pass
