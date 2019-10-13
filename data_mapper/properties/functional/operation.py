from typing import Callable, Iterable

from data_mapper.errors import PropertyNotResolved
from data_mapper.properties import Property
from data_mapper.properties.abstract import AbstractProperty


class Operation(Property):
    default_sources = []

    def __init__(
            self,
            *props: AbstractProperty or Iterable[AbstractProperty],
            props_it: (Iterable[AbstractProperty] or
                       Iterable[Iterable[AbstractProperty]]) = None,
            star_func: Callable = None,
            func: Callable = None,
            **kwargs,
    ):
        if not hasattr(self, 'star_func'):
            self.star_func = star_func

        if not hasattr(self, 'func'):
            self.func = func

        assert self.star_func is None or self.func is None, \
            'star_func and func exclusive'

        super().__init__(*props, sources_it=props_it, **kwargs)

    def apply(self, *args):
        if self.star_func is not None:
            return self.star_func(*args)
        if self.func is not None:
            return self.func(args)
        raise NotImplementedError

    def get(self, data, result=None):
        try:
            value = self.apply(*self.get_args(data, result))
        except self.get_value_exc as e:
            value = self.value_if_not_found(errors=[e], result=result)
        return value

    def get_args(self, data, result=None):
        for props in self.get_sources():
            if isinstance(props, AbstractProperty):
                yield props.get(data, result)
            else:
                errors = []
                for prop in props:
                    try:
                        yield prop.get(data, result)
                    except self.get_value_exc as e:
                        errors.append(e)
                        continue
                    else:
                        break
                else:
                    raise PropertyNotResolved(self, errors)
