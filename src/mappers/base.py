from abc import abstractmethod
from typing import Iterable, Tuple, Any, Iterator, Dict

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
        return MapResult(self, data)


class MapResult:
    result = {}

    def __init__(self, mapper: MapperBase, data: Dict):
        self.mapper = mapper
        self.data = data

    def __iter__(self) -> Iterator[Tuple[Any, Any]]:
        return (
            (key, self.result.get(key, self[key]))
            for key in self.mapper.properties.keys()
        )

    def __getitem__(self, item):
        try:
            value = self.result[item]
        except KeyError:
            value = self.mapper.properties[item].get(self.data)
            self.result[item] = value
        return value


class Mapper(MapperBase):
    def get_properties(self) -> Iterable[Tuple[Any, AbstractProperty]]:
        for key, prop in self.__class__.__dict__.items():
            if isinstance(prop, AbstractProperty):
                if prop.sources is None:
                    prop.sources = [key]
                yield (key, prop)
