from typing import Iterable, Callable

from data_mapper.errors import PropertyNotResolved
from data_mapper.properties.abstract import AbstractProperty
from data_mapper.properties.operations import AllOperations
from data_mapper.utils import NOT_SET, cached_property


class Property(AllOperations):
    default_sources = [[]]
    get_value_exc_default = (LookupError, AttributeError, ValueError, TypeError)

    def __init__(
            self,
            *sources,
            sources_it: Iterable = None,
            default=NOT_SET,
            required: bool = None,
            get_value: Callable = None,
            get_value_exc=None,
    ):
        assert not sources or not sources_it, \
            '*sources and sources_it are exclusive'
        assert default is NOT_SET or not required

        if len(sources) > 0:
            self.sources = sources
        elif sources_it is not None:
            self.sources = sources_it
        else:
            self.sources = None

        self.default = default
        self.required = True if required is None else required
        self._get_value = get_value
        self._get_value_exc = get_value_exc
        self.parent = None

    def get(self, data, result=None):
        sources = self.get_sources()

        for source in sources:
            value = data
            try:
                if isinstance(source, AbstractProperty):
                    value = source.get(value, result)
                elif isinstance(source, str) or not hasattr(source, '__iter__'):
                    value = self.get_value(value, source)
                else:
                    for sub_source in source:
                        if isinstance(sub_source, AbstractProperty):
                            value = sub_source.get(value, result)
                        else:
                            value = self.get_value(value, sub_source)
                value = self.eval(
                    value,
                    result=result,
                    sources=sources,
                    current_source=source,
                )
            except self.get_value_exc:
                continue
            else:
                break
        else:
            value = self.value_if_not_found(sources)

        return value

    def value_if_not_found(self, sources=NOT_SET):
        if sources is NOT_SET:
            sources = self.get_sources()
        if self.default is not NOT_SET:
            value = self.default
        elif self.required:
            raise PropertyNotResolved(self)
        else:
            value = None
        return value

    def get_sources(self):
        return self.default_sources if self.sources is None else self.sources

    def eval(self, value, **context):
        if value is None:
            # noinspection PyNoneFunctionAssignment
            value = self.eval_none(**context)
        else:
            value = self.eval_not_none(value, **context)
        return value

    def eval_none(self, **context):
        return

    def eval_not_none(self, value, **context):
        return value

    @cached_property
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

    @cached_property
    def get_value_exc(self):
        get_value_exc = self._get_value_exc
        if get_value_exc is None and self.parent is not None:
            get_value_exc = self.parent.get_value_exc
        if get_value_exc is None:
            get_value_exc = self.get_value_exc_default
        return get_value_exc

    def __str__(self):
        if self.sources is None:
            sources_str = ''
        else:
            sources_str = ",".join(map(repr, self.sources))
        return f'{self.__class__.__name__}({sources_str})'
