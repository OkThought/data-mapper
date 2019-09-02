from .properties import (
    Property,
    Value,
    PropertyRef,
)

from .properties.functional import (
    Operation,
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
