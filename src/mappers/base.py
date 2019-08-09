from abc import abstractmethod
from typing import Iterable, Tuple, Any, Dict

from src.properties.abstract import AbstractProperty
from src.utils import cached_property


class MapperBase:
    @cached_property
    def properties(self):
        return dict(self.get_properties())

    @abstractmethod
    def get_properties(self) -> Iterable[Tuple[Any, AbstractProperty]]:
        pass

    def map(self, data: Dict):
        from src.mappers.result import MapResult
        return MapResult(self, data)
