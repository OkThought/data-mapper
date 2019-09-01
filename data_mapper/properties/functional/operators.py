from operator import (
    lt, le, eq, ne, ge, gt,

    not_, truth, is_, is_not,

    abs, add, and_, floordiv, index, inv, lshift, mod, mul, matmul, neg, or_,
    pos, pow, rshift, sub, truediv, xor,

    concat, contains, countOf, delitem, getitem, indexOf, setitem,
)

from data_mapper.properties.functional.binary_operation import BinaryOperation
from data_mapper.properties.functional.ternary_operation import TernaryOperation
from data_mapper.properties.functional.unary_operation import UnaryOperation


__all__ = [
    'Lt',
    'Le',
    'Eq',
    'Ne',
    'Ge',
    'Gt',
    'Not',
    'Truth',
    'Is',
    'IsNot',
    'Abs',
    'Index',
    'Inv',
    'Neg',
    'Pos',
    'Add',
    'And',
    'Floordiv',
    'Lshift',
    'Mod',
    'Mul',
    'Matmul',
    'Or',
    'Pow',
    'Rshift',
    'Sub',
    'Truediv',
    'Xor',
    'Concat',
    'Contains',
    'CountOf',
    'Delitem',
    'Getitem',
    'IndexOf',
    'Setitem',
]


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


# Logical Unary Operations ****************************************************#

class Not(UnaryOperation):
    star_func = not_


class Truth(UnaryOperation):
    star_func = truth


# Logical Binary Operations ***************************************************#

class Is(BinaryOperation):
    star_func = is_


class IsNot(BinaryOperation):
    star_func = is_not


# Mathematical/Bitwise Unary Operations ***************************************#

class Abs(UnaryOperation):
    star_func = abs


class Index(UnaryOperation):
    star_func = index


class Inv(UnaryOperation):
    star_func = inv


class Neg(UnaryOperation):
    star_func = neg


class Pos(UnaryOperation):
    star_func = pos


# Mathematical/Bitwise Binary Operations **************************************#

class Add(BinaryOperation):
    star_func = add


class And(BinaryOperation):
    star_func = and_


class Floordiv(BinaryOperation):
    star_func = floordiv


class Lshift(BinaryOperation):
    star_func = lshift


class Mod(BinaryOperation):
    star_func = mod


class Mul(BinaryOperation):
    star_func = mul


class Matmul(BinaryOperation):
    star_func = matmul


class Or(BinaryOperation):
    star_func = or_


class Pow(BinaryOperation):
    star_func = pow


class Rshift(BinaryOperation):
    star_func = rshift


class Sub(BinaryOperation):
    star_func = sub


class Truediv(BinaryOperation):
    star_func = truediv


class Xor(BinaryOperation):
    star_func = xor


# Sequence Binary Operations **************************************************#


class Concat(BinaryOperation):
    star_func = concat


class Contains(BinaryOperation):
    star_func = contains


class CountOf(BinaryOperation):
    star_func = countOf


class Delitem(BinaryOperation):
    star_func = delitem


class Getitem(BinaryOperation):
    star_func = getitem


class IndexOf(BinaryOperation):
    star_func = indexOf


# Sequence Ternary Operations *************************************************#


class Setitem(TernaryOperation):
    star_func = setitem
