from abc import abstractmethod
from typing import Iterable, Tuple, Any, Dict

from src.properties.abstract import AbstractProperty
from src.utils import cached_property


class MapperBase(AbstractProperty):
    @cached_property
    def props_map(self):
        return dict(self.get_props_map())

    @abstractmethod
    def get_props_map(self) -> Iterable[Tuple[Any, AbstractProperty]]:
        pass

    def get(self, data: Dict, result=None):
        from src.mappers.result import MapResult
        return MapResult(self, data)
