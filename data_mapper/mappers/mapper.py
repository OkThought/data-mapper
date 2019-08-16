from typing import Iterable, Tuple, Any

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

    def _get_class_props(self) -> Iterable[Tuple[Any, AbstractProperty]]:
        for key, prop in self.__class__.__dict__.items():
            if isinstance(prop, AbstractProperty):
                self.configure_prop(prop, key)
                yield (key, prop)
