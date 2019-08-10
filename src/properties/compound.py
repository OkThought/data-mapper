from typing import Any, Mapping

from src.mappers.result import MapResult
from src.properties.abstract import AbstractProperty
from src.properties.property import Property


class CompoundProperty(Property):
    def __init__(
            self,
            *args,
            props_map: Mapping[Any, AbstractProperty],
            lazy: bool = True,
            **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.props_map = props_map
        self.lazy = lazy

    def get_raw(self, data, result=None):
        result = MapResult(
            self.props_map,
            data=super().get_raw(data, result),
            lazy=self.lazy,
        )
        return result
