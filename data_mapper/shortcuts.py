from data_mapper.properties import (
    IntegerProperty, FloatProperty, DictProperty,
    StringProperty,
    ListProperty,
    CompoundProperty,
    CompoundListProperty,
    BooleanProperty,
    Property,
    Value,
    PropertyRef,
)

from data_mapper.properties.functional import (
    Operation,
    FunctionProperty,
)

P = Property
V = Value
Op = Operation
F = FunctionProperty
R = PropertyRef
Bool = Boolean = BooleanProperty
Str = StringProperty
Int = IntegerProperty
Float = FloatProperty
Dict = DictProperty
List = ListProperty
D = CompoundProperty
L = CompoundListProperty
