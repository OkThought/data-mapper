from abc import ABC
from operator import (
    lt, le, eq, ne, ge, gt,

    not_, truth, is_, is_not,

    abs, add, and_, floordiv, index, inv, lshift, mod, mul, matmul, neg, or_,
    pos, pow, rshift, sub, truediv, xor,

    concat, contains, countOf, getitem, indexOf,
)

from data_mapper.properties import Value
from data_mapper.properties.abstract import AbstractProperty
from data_mapper.properties.functional.binary_operation import BinaryOperation
from data_mapper.properties.functional.ternary_operation import TernaryOperation
from data_mapper.properties.functional.unary_operation import UnaryOperation

__all__ = [
    'AllOperations',
    'ComparisonOperations',
    'Lt',
    'Le',
    'Eq',
    'Ne',
    'Ge',
    'Gt',
    'LogicalOperations',
    'LogicalUnaryOperations',
    'Not',
    'Truth',
    'LogicalBinaryOperations',
    'Is',
    'IsNot',
    'MathOperations',
    'MathUnaryOperations',
    'Abs',
    'Index',
    'Neg',
    'Pos',
    'MathBinaryOperations',
    'Add',
    'Floordiv',
    'Mod',
    'Mul',
    'Matmul',
    'Pow',
    'Sub',
    'Truediv',
    'BitwiseOperations',
    'BitwiseUnaryOperations',
    'Inv',
    'BitwiseBinaryOperations',
    'And',
    'Lshift',
    'Or',
    'Rshift',
    'Xor',
    'SequenceOperations',
    'SequenceBinaryOperations',
    'Concat',
    'Contains',
    'CountOf',
    'Delitem',
    'Getitem',
    'IndexOf',
    'SequenceTernaryOperations',
    'Setitem',
]


def _make_prop(obj):
    if not isinstance(obj, AbstractProperty):
        obj = Value(obj)
    return obj


# Comparison Operations *******************************************************#

class Lt(BinaryOperation):
    star_func = lt


class Le(BinaryOperation):
    star_func = le


class Eq(BinaryOperation):
    star_func = eq


class Ne(BinaryOperation):
    star_func = ne


class Ge(BinaryOperation):
    star_func = ge


class Gt(BinaryOperation):
    star_func = gt


class ComparisonOperations(AbstractProperty, ABC):
    def __lt__(self, other):
        return Lt(self, _make_prop(other))

    def __le__(self, other):
        return Le(self, _make_prop(other))

    def __eq__(self, other):
        return Eq(self, _make_prop(other))

    def __ne__(self, other):
        return Ne(self, _make_prop(other))

    def __ge__(self, other):
        return Ge(self, _make_prop(other))

    def __gt__(self, other):
        return Gt(self, _make_prop(other))


# Logical Unary Operations ****************************************************#

class Not(UnaryOperation):
    star_func = not_


class Truth(UnaryOperation):
    star_func = truth


class LogicalUnaryOperations(AbstractProperty, ABC):
    def __not__(self):
        return Not(self)

    def truth(self):
        return Truth(self)


# Logical Binary Operations ***************************************************#

class Is(BinaryOperation):
    star_func = is_


class IsNot(BinaryOperation):
    star_func = is_not


class LogicalBinaryOperations(AbstractProperty, ABC):
    def is_(self, other):
        return Is(self, _make_prop(other))

    def is_not(self, other):
        return IsNot(self, _make_prop(other))


class LogicalOperations(
    LogicalUnaryOperations,
    LogicalBinaryOperations,
    ABC,
):
    pass


# Mathematical Unary Operations ***************************************#

class Abs(UnaryOperation):
    star_func = abs


class Index(UnaryOperation):
    star_func = index


class Neg(UnaryOperation):
    star_func = neg


class Pos(UnaryOperation):
    star_func = pos


class MathUnaryOperations(AbstractProperty, ABC):
    def __abs__(self):
        return Abs(self)

    def __index__(self):
        return Index(self)

    def __neg__(self):
        return Neg(self)

    def __pos__(self):
        return Pos(self)


# Mathematical Binary Operations **************************************#

class Add(BinaryOperation):
    star_func = add


class Floordiv(BinaryOperation):
    star_func = floordiv


class Mod(BinaryOperation):
    star_func = mod


class Mul(BinaryOperation):
    star_func = mul


class Matmul(BinaryOperation):
    star_func = matmul


class Pow(BinaryOperation):
    star_func = pow


class Sub(BinaryOperation):
    star_func = sub


class Truediv(BinaryOperation):
    star_func = truediv


class MathBinaryOperations(AbstractProperty, ABC):
    def __add__(self, other):
        return Add(self, _make_prop(other))

    def __floordiv__(self, other):
        return Floordiv(self, _make_prop(other))

    def __mod__(self, other):
        return Mod(self, _make_prop(other))

    def __mul__(self, other):
        return Mul(self, _make_prop(other))

    def __matmul__(self, other):
        return Matmul(self, _make_prop(other))

    def __pow__(self, other):
        return Pow(self, _make_prop(other))

    def __sub__(self, other):
        return Sub(self, _make_prop(other))

    def __truediv__(self, other):
        return Truediv(self, _make_prop(other))


class MathOperations(
    MathUnaryOperations,
    MathBinaryOperations,
    ABC,
):
    pass


# Bitwise Unary Operations ***************************************#

class Inv(UnaryOperation):
    star_func = inv


class BitwiseUnaryOperations(AbstractProperty, ABC):
    def __invert__(self):
        return Inv(self)


# Bitwise Binary Operations **************************************#

class And(BinaryOperation):
    star_func = and_


class Lshift(BinaryOperation):
    star_func = lshift


class Or(BinaryOperation):
    star_func = or_


class Rshift(BinaryOperation):
    star_func = rshift


class Xor(BinaryOperation):
    star_func = xor


class BitwiseBinaryOperations(AbstractProperty, ABC):
    def __and__(self, other):
        return And(self, _make_prop(other))

    def __lshift__(self, other):
        return Lshift(self, _make_prop(other))

    def __or__(self, other):
        return Or(self, _make_prop(other))

    def __rshift__(self, other):
        return Rshift(self, _make_prop(other))

    def __xor__(self, other):
        return Xor(self, _make_prop(other))


class BitwiseOperations(
    BitwiseUnaryOperations,
    BitwiseBinaryOperations,
    ABC,
):
    pass


# Sequence Binary Operations **************************************************#


class Concat(BinaryOperation):
    star_func = concat


class Contains(BinaryOperation):
    star_func = contains


class CountOf(BinaryOperation):
    star_func = countOf


class Delitem(BinaryOperation):
    @staticmethod
    def star_func(o, k):
        del o[k]
        return o


class Getitem(BinaryOperation):
    star_func = getitem


class IndexOf(BinaryOperation):
    star_func = indexOf


class SequenceBinaryOperations(AbstractProperty, ABC):
    def concat(self, other):
        return Concat(self, _make_prop(other))

    def contains(self, other):
        return Contains(self, _make_prop(other))

    def count_of(self, other):
        return CountOf(self, _make_prop(other))

    def delitem(self, other):
        return Delitem(self, _make_prop(other))

    def index_of(self, other):
        return IndexOf(self, _make_prop(other))

    def __getitem__(self, key):
        return Getitem(self, _make_prop(key))


# Sequence Ternary Operations *************************************************#

class Setitem(TernaryOperation):
    @staticmethod
    def star_func(o, k, v):
        o[k] = v
        return o


class SequenceTernaryOperations(AbstractProperty, ABC):
    def set(self, key, val):
        return Setitem(self, _make_prop(key), _make_prop(val))


class SequenceOperations(
    SequenceBinaryOperations,
    SequenceTernaryOperations,
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
