from typing import Callable, Iterable

from data_mapper.errors import PropertyNotFound
from data_mapper.properties import Property
from data_mapper.properties.abstract import AbstractProperty


class Operation(Property):
    star_func = None
    func = None

    def __init__(
            self,
            *props: AbstractProperty or Iterable[AbstractProperty],
            props_it: (Iterable[AbstractProperty] or
                       Iterable[Iterable[AbstractProperty]]) = None,
            star_func: Callable = None,
            func: Callable = None,
            **kwargs,
    ):
        assert star_func is None or func is None

        if star_func is not None:
            self.star_func = star_func

        if func is not None:
            self.func = func

        super().__init__(*props, sources_it=props_it, **kwargs)

    def apply(self, *args):
        if self.star_func is not None:
            return self.star_func(*args)
        if self.func is not None:
            return self.func(args)
        raise NotImplementedError

    def get_raw(self, data, result=None):
        return self.apply(*self.get_args(data, result))

    def get_args(self, data, result=None):
        sources = self.sources
        if sources is None:
            sources = []

        for props in sources:
            if isinstance(props, AbstractProperty):
                yield props.get(data, result)
            else:
                for prop in props:
                    try:
                        yield prop.get(data, result)
                    except PropertyNotFound:
                        continue
                    else:
                        break
                else:
                    raise PropertyNotFound(props)
