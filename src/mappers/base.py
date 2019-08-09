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


class Mapper(MapperBase):
    def get_properties(self) -> Iterable[Tuple[Any, AbstractProperty]]:
        for key, prop in self.__class__.__dict__.items():
            if isinstance(prop, AbstractProperty):
                if prop.sources is None:
                    prop.sources = [key]
                yield (key, prop)
