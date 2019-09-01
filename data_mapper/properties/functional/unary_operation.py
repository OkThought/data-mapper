from data_mapper.properties.abstract import AbstractProperty
from data_mapper.properties.functional.operation import Operation


class UnaryOperation(Operation):
    def __init__(
            self,
            prop: AbstractProperty,
            **kwargs,
    ):
        super().__init__(prop, **kwargs)
