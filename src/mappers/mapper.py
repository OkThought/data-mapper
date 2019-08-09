from typing import Iterable, Tuple, Any

from src.mappers.base import MapperBase
from src.properties.abstract import AbstractProperty


class Mapper(MapperBase):
    def get_props_map(self) -> Iterable[Tuple[Any, AbstractProperty]]:
        for key, prop in self.__class__.__dict__.items():
            if isinstance(prop, AbstractProperty):
                if prop.sources is None:
                    prop.sources = [key]
                yield (key, prop)
