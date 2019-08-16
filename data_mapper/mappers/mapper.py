from typing import Iterable, Tuple, Any, Mapping

from data_mapper.properties.abstract import AbstractProperty
from data_mapper.properties.compound import CompoundProperty


class Mapper(CompoundProperty):
    def __init__(
            self,
            _options: dict = None,
            **props_map,
    ):
        props_map = props_map or dict(self._get_class_props())
        super().__init__(_options, **props_map)

    @classmethod
    def _get_class_props(cls) -> Iterable[Tuple[Any, AbstractProperty]]:
        for key, prop in cls.__dict__.items():
            if isinstance(prop, AbstractProperty):
                cls.configure_prop_sources(prop, key)
                yield (key, prop)
