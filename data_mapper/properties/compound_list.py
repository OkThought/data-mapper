from typing import Iterable

from data_mapper.properties import Property
from data_mapper.properties.abstract import AbstractProperty


class CompoundListProperty(Property):
    default_sources = []

    def __init__(
            self,
            *props,
            skip_none: bool = False,
            props_it: Iterable = None,
            sources_it: Iterable = None,
            **kwargs,
    ):
        if sources_it:
            props = sources_it

        if props_it:
            props = props_it

        from data_mapper.properties import Value

        props = ((
            prop if isinstance(prop, AbstractProperty)
            else Property(*(
                sub_prop if isinstance(sub_prop, AbstractProperty)
                else Value(sub_prop)
                for sub_prop in prop
            )) if hasattr(prop, '__iter__')
            else Value(prop)
        ) for prop in props)
        super().__init__(*props, **kwargs)
        self.skip_none = skip_none
        self.values = None

    def get(self, data, result=None):
        self.values = []
        value = super().get(data, result)
        if self.skip_none:
            value = [i for i in value if i is not None]
        return value

    def should_stop(self, **context):
        return False

    def handle_error(self, e: BaseException, *args, errors, **context):
        raise e

    def value_if_not_found(self, errors=None, **context):
        return self.values

    def eval_not_none(self, value, **context):
        self.values.append(value)
        return value

    def eval_none(self, **context):
        if not self.skip_none:
            self.values.append(None)
        return None
