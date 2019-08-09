from typing import Dict, Iterator, Tuple, Any

from src.mappers.base import MapperBase


class MapResult:
    def __init__(self, mapper: MapperBase, data: Dict):
        self.mapper = mapper
        self.data = data
        self.result = {}

    def keys(self):
        return self.mapper.props_map.keys()

    def __iter__(self) -> Iterator[Tuple[Any, Any]]:
        return (
            (key, self[key])
            for key in self.mapper.props_map.keys()
        )

    def __getitem__(self, item):
        try:
            value = self.result[item]
        except KeyError:
            value = self.mapper.props_map[item].get(self.data)
            self.result[item] = value
        return value
