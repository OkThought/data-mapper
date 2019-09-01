from data_mapper.properties import Property
from data_mapper.properties.functional.operation import Operation


class BinaryOperation(Operation):
    def __init__(
            self,
            prop1: Property,
            prop2: Property,
            **kwargs,
    ):
        super().__init__(prop1, prop2, **kwargs)
