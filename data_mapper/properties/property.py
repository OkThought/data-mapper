from typing import Iterable, Callable

from data_mapper.errors import PropertyNotFound
from data_mapper.properties.abstract import AbstractProperty
from data_mapper.properties.operations import AllOperations
from data_mapper.utils import NOT_SET


class Property(AllOperations):
    default_sources = [[]]
    get_value_exc_default = (LookupError, AttributeError)

    def __init__(
            self,
            *sources,
            sources_it: Iterable = None,
            default=NOT_SET,
            required: bool = None,
            transforms: Iterable[Callable[[str], str]] = None,
            get_value: Callable = None,
            get_value_exc=None,
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
        self._get_value = get_value
        self._get_value_exc = get_value_exc
        self.parent = None

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
        sources = self.get_sources()

        for source in sources:
            value = data
            try:
                if isinstance(source, AbstractProperty):
                    value = source.get(value)
                elif isinstance(source, str) or not hasattr(source, '__iter__'):
                    value = self.get_value(value, source)
                else:
                    for sub_source in source:
                        if isinstance(sub_source, AbstractProperty):
                            value = sub_source.get(value)
                        else:
                            value = self.get_value(value, sub_source)
            except self.get_value_exc:
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

    def get_sources(self):
        return self.default_sources if self.sources is None else self.sources

    @property
    def get_value(self):
        get_value = self._get_value
        if get_value is None and self.parent is not None:
            get_value = self.parent.get_value
        if get_value is None:
            get_value = self.get_value_default
        return get_value

    @staticmethod
    def get_value_default(d, k):
        try:
            return d[k]
        except (LookupError, TypeError) as e:
            if isinstance(k, str):
                return getattr(d, k)
            raise e

    @property
    def get_value_exc(self):
        get_value_exc = self._get_value_exc
        if get_value_exc is None and self.parent is not None:
            get_value_exc = self.parent.get_value_exc
        if get_value_exc is None:
            get_value_exc = self.get_value_exc_default
        return get_value_exc

    def __str__(self):
        if self.sources is None:
            sources_str = str(self.sources)
        else:
            sources_str = ",".join(map(repr, self.sources))
        return f'{self.__class__.__name__}<{sources_str}>'
