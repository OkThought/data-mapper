from .properties import (
    Property,
    Value,
    PropertyRef,
)

from .properties.functional import (
    Operation,
    FunctionProperty,
)

from .properties.functional.operators import AllOperations


class P(Property, AllOperations):
    pass


class V(Value, AllOperations):
    pass


class R(PropertyRef, AllOperations):
    pass


class Op(Operation, AllOperations):
    pass


class F(FunctionProperty, AllOperations):
    pass
