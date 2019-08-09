from typing import Iterable

from src.errors import PropertyNotFound
from src.properties.transformable import TransformableProperty
from src.utils import NOT_SET


class Property(TransformableProperty):
    required = True
    default = NOT_SET
    sources = None

    def __init__(
            self,
            sources: Iterable = NOT_SET,
            default=NOT_SET,
            required: bool = NOT_SET,
            **kwargs,
    ):
        super().__init__(**kwargs)

        if sources is not NOT_SET:
            self.sources = sources

        assert default is NOT_SET or not required

        if default is not NOT_SET:
            self.default = default
        if self.required is not NOT_SET:
            self.required = required

    def get(self, data: dict):
        value = self.get_raw(data)
        value = self.transform(value)
        return value

    def get_raw(self, src: dict):
        assert self.sources, \
            'sources must be defined before getting property value'

        for source in self.sources:
            try:
                value = src[source]
            except KeyError:
                continue
            else:
                break
        else:
            if self.default is not NOT_SET:
                value = self.default
            elif self.required:
                raise PropertyNotFound(self.sources)
            else:
                value = None

        return value
