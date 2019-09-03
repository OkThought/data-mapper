from typing import Callable, Iterable, Mapping

from data_mapper.properties import CompoundProperty
from data_mapper.properties.abstract import AbstractProperty


class FunctionProperty(CompoundProperty):
    def __init__(
            self,
            func: Callable = None,
            *pos_args: AbstractProperty,
            args: AbstractProperty or Iterable[AbstractProperty] = None,
            kwargs: AbstractProperty or Mapping[AbstractProperty] = None,
            **options,
    ):
        assert sum(1 for i in (pos_args, args) if i) <= 1, \
            '*pos_args and args are exclusive'

        props_map = {}

        if pos_args:
            args = pos_args

        if args is not None:
            if not isinstance(args, AbstractProperty):
                from data_mapper.properties import CompoundListProperty
                args = CompoundListProperty(props_it=args)
            props_map['args'] = args
        if kwargs is not None:
            if not isinstance(kwargs, AbstractProperty):
                kwargs = CompoundProperty(**kwargs)
            props_map['kwargs'] = kwargs
        super().__init__(
            options,
            **props_map,
        )
        self.func = func

    def eval_not_none(self, value, result=None, **context):
        value = super().eval_not_none(value, result=result, **context)
        value = self.func(*value.get('args', ()), **value.get('kwargs', {}))
        return value
