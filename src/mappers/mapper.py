from abc import abstractmethod
from typing import Iterable, Tuple, Any, Dict

from src.properties.abstract import AbstractProperty
from src.utils import cached_property


class Mapper(AbstractProperty):
    @cached_property
    def props_map(self):
        return dict(self.get_props_map())

    def get(self, data: Dict, result=None):
        from src.mappers.result import MapResult
        return MapResult(self, data)

    def get_props_map(self) -> Iterable[Tuple[Any, AbstractProperty]]:
        for key, prop in self.__class__.__dict__.items():
            if isinstance(prop, AbstractProperty):
                if getattr(prop, 'sources', 0) is None:
                    prop.sources = [key]
                yield (key, prop)
