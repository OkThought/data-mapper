from data_mapper.properties.abstract import AbstractProperty
from data_mapper.properties.functional import Operation


class TernaryOperation(Operation):

    def __init__(
            self,
            prop1: AbstractProperty,
            prop2: AbstractProperty,
            prop3: AbstractProperty,
            **kwargs,
    ):
        super().__init__(prop1, prop2, prop3, **kwargs)
