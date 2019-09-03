from .properties import (
    Property,
    Value,
    PropertyRef,
)

from .properties.functional import (
    Operation,
    FunctionProperty,
)

from data_mapper.properties.operations import AllOperations


P = Property
V = Value
Op = Operation
F = FunctionProperty


class R(PropertyRef, AllOperations):
    pass
