from typing import Any, Collection

from data_mapper.properties.abstract import AbstractProperty


class PropertyRef(AbstractProperty):
    def __init__(self, source: Collection[Any]):
        assert len(source) > 0
        self.source = source

    def get(self, data, result=None):
        value = result
        for sub_source in self.source:
            value = value[sub_source]
        return value
