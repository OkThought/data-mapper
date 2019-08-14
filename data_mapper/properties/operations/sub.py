from data_mapper.properties.operations.binary_operation import BinaryOperation


class Sub(BinaryOperation):

    def apply(self, a, b):
        return a - b
