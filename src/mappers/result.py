from typing import Dict, Iterator, Tuple, Any

from src.mappers.base import MapperBase


class MapResult:
    result = {}

    def __init__(self, mapper: MapperBase, data: Dict):
        self.mapper = mapper
        self.data = data

    def keys(self):
        return self.mapper.properties.keys()

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
