from typing import Iterable, Callable

from data_mapper.properties import Property


class Value(Property):
    def __init__(self, value, **kwargs):
        self.value = value
        super().__init__(**kwargs)

    def get_raw(self, data, result=None):
        return self.value


V = Value
