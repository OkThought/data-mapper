from typing import Callable, Iterable, Mapping

from data_mapper.properties import CompoundProperty
from data_mapper.properties.abstract import AbstractProperty


class FunctionProperty(CompoundProperty):
    def __init__(
            self,
            func: Callable = None,
            args: AbstractProperty or Iterable[AbstractProperty] = None,
            kwargs: AbstractProperty or Mapping[AbstractProperty] = None,
            **options,
    ):
        props_map = {}
        if args is not None:
            if not isinstance(args, AbstractProperty):
                from data_mapper.properties import CompoundListProperty
                args = CompoundListProperty(props_it=args, default=())
            props_map['args'] = args
        if kwargs is not None:
            if not isinstance(kwargs, AbstractProperty):
                kwargs = CompoundProperty(**kwargs, default={})
            props_map['kwargs'] = kwargs
        super().__init__(
            options,
            **props_map,
        )
        self.func = func

    def get(self, data, result=None):
        value = super().get(data, result)
        value = self.func(*value.get('args', ()), **value.get('kwargs', {}))
        return value
