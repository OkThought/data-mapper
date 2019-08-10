from typing import Iterable, Callable

from src.errors import PropertyNotFound
from src.properties.abstract import AbstractProperty
from src.utils import NOT_SET


class Property(AbstractProperty):
    required = True
    default = NOT_SET
    sources = None
    transforms = []

    def __init__(
            self,
            sources: Iterable = NOT_SET,
            default=NOT_SET,
            required: bool = NOT_SET,
            transforms: Iterable[Callable[[str], str]] = NOT_SET,
            **kwargs,
    ):
        assert default is NOT_SET or not required

        super().__init__(**kwargs)

        if sources is not NOT_SET:
            self.sources = sources

        if default is not NOT_SET:
            self.default = default

        if self.required is not NOT_SET:
            self.required = required

        if transforms is not NOT_SET:
            self.transforms = transforms

    def get(self, data: dict, result=None):
        value = self.get_raw(data, result)
        self.validate_raw(value)
        value = self.transform(value)
        self.validate(value)
        return value

    def transform(self, value):
        for transform in self.get_transforms():
            value = transform(value)
        return value

    def get_transforms(self):
        return self.transforms

    def get_raw(self, data: dict, result=None):
        assert self.sources, \
            'sources must be defined before getting property value'

        for source in self.sources:
            try:
                value = data[source]
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
