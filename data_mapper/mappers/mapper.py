from typing import Iterable, Tuple, Any, Mapping

from data_mapper.properties.abstract import AbstractProperty
from data_mapper.properties.compound import CompoundProperty


class Mapper(CompoundProperty):
    def __init__(
            self,
            *args,
            props_map: Mapping[Any, AbstractProperty] = None,
            **kwargs,
    ):
        if props_map is None:
            props_map = dict(self._get_class_props())
        super().__init__(*args, props_map=props_map, **kwargs)

    @classmethod
    def _get_class_props(cls) -> Iterable[Tuple[Any, AbstractProperty]]:
        for key, prop in cls.__dict__.items():
            if isinstance(prop, AbstractProperty):
                if getattr(prop, 'sources', 0) is None:
                    prop.sources = [key]
                yield (key, prop)
