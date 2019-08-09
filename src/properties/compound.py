from typing import Iterable, Tuple, Any, Mapping

from src.mappers.mapper import Mapper
from src.properties.abstract import AbstractProperty


class CompoundProperty(Mapper):
    def __init__(
            self,
            props_map: Mapping[Any, AbstractProperty],
    ):
        self._props_map = props_map
        super().__init__()

    def get_props_map(self) -> Iterable[Tuple[Any, AbstractProperty]]:
        return self._props_map.items()

    @property
    def props_map(self):
        return self._props_map
