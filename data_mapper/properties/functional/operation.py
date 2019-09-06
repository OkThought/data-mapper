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

        self.configure_props()

    def configure_props(self):
        for source in self.get_sources():
            if isinstance(source, AbstractProperty):
                self.configure_prop(source)
            else:
                for prop in source:
                    self.configure_prop(prop)

    def configure_prop(self, prop):
        if isinstance(prop, Property):
            prop.parent = self

    def apply(self, *args):
        if self.star_func is not None:
            return self.star_func(*args)
        if self.func is not None:
            return self.func(args)
        raise NotImplementedError

    def get(self, data, result=None):
        return self.apply(*self.get_args(data, result))

    def get_args(self, data, result=None):
        for props in self.get_sources():
            if isinstance(props, AbstractProperty):
                yield props.get(data, result)
            else:
                for prop in props:
                    try:
                        yield prop.get(data, result)
                    except PropertyNotResolved:
                        continue
                    else:
                        break
                else:
                    raise PropertyNotResolved(self)
