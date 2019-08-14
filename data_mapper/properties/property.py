from typing import Iterable, Callable

from data_mapper.errors import PropertyNotFound
from data_mapper.properties.abstract import AbstractProperty
from data_mapper.utils import NOT_SET


class Property(AbstractProperty):
    def __init__(
            self,
            *sources,
            sources_it: Iterable = None,
            default=NOT_SET,
            required: bool = None,
            transforms: Iterable[Callable[[str], str]] = None,
            **kwargs,
    ):
        assert not sources or not sources_it, \
            '*sources and sources_it are exclusive'
        assert default is NOT_SET or not required

        super().__init__(**kwargs)

        if len(sources) > 0:
            self.sources = sources
        elif sources_it is not None:
            self.sources = sources_it
        else:
            self.sources = None

        self.default = default
        self.required = True if required is None else required
        self.transforms = [] if transforms is None else transforms

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
                if isinstance(source, str) or not hasattr(source, '__iter__'):
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

    def __str__(self):
        if self.sources is None:
            sources_str = str(self.sources)
        else:
            sources_str = ",".join(map(repr, self.sources))
        return f'{self.__class__.__name__}<{sources_str}>'

    def __sub__(self, other):
        from data_mapper.properties.operations.sub import Sub
        return Sub(self, other)

    def __add__(self, other):
        from data_mapper.properties.operations.add import Add
        return Add(self, other)

    def __mul__(self, other):
        from data_mapper.properties.operations.mul import Mul
        return Mul(self, other)

    def __truediv__(self, other):
        from data_mapper.properties.operations.div import Div
        return Div(self, other)
