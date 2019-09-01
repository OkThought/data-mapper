from data_mapper.properties.functional.binary_operation import BinaryOperation


class Mul(BinaryOperation):

    def apply(self, a, b):
        return a * b
