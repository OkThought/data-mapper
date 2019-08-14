from data_mapper.properties.operations.binary_operation import BinaryOperation


class Add(BinaryOperation):

    def apply(self, a, b):
        return a + b
