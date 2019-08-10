from typing import Any, Mapping

from src.mappers.result import MapResult
from src.properties.abstract import AbstractProperty
from src.properties.property import Property


class CompoundProperty(Property):
    sources = [[]]

    def __init__(
            self,
            *args,
            props_map: Mapping[Any, AbstractProperty],
            **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.props_map = props_map

    def get(self, data, result=None):
        return MapResult(self.props_map, super().get(data, result))
