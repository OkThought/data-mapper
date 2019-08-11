from typing import Iterable, Callable

from data_mapper.errors import PropertyNotFound
from data_mapper.properties.abstract import AbstractProperty
from data_mapper.utils import NOT_SET


class Property(AbstractProperty):
    required = True
    default = NOT_SET
    sources = None
    transforms = []

    def __init__(
            self,
            *sources: Iterable,
            default=NOT_SET,
            required: bool = NOT_SET,
            transforms: Iterable[Callable[[str], str]] = NOT_SET,
            **kwargs,
    ):
        assert default is NOT_SET or not required

        super().__init__(**kwargs)

        if len(sources) > 0:
            self.sources = list(sources)

        if default is not NOT_SET:
            self.default = default

        if self.required is not NOT_SET:
            self.required = required

        if transforms is not NOT_SET:
            self.transforms = transforms

    def get(self, data, result=None):
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

    def get_raw(self, data, result=None):
        sources = self.sources
        if sources is None:
            sources = [[]]

        for source in sources:
            value = data
            try:
                if isinstance(source, str):
                    value = value[source]
                else:
                    for sub_source in source:
                        value = value[sub_source]
            except KeyError:
                continue
            else:
                break
        else:
            if self.default is not NOT_SET:
                value = self.default
            elif self.required:
                raise PropertyNotFound(sources)
            else:
                value = None

        return value
