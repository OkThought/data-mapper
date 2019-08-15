from typing import Callable

from data_mapper.mappers import Mapper
from data_mapper.properties.abstract import AbstractProperty


class ObjectMapper(Mapper):
    def __init__(
            self,
            *_args,
            init: Callable = None,
            args: AbstractProperty = None,
            kwargs: AbstractProperty = None,
            **_kwargs,
    ):
        super().__init__(*_args, **_kwargs)

        if init is not None:
            self.init = init
        assert hasattr(self, 'init') and self.init is not None

        if args is not None:
            self.args = args
        elif not hasattr(self, 'args'):
            self.args = None

        if kwargs is not None:
            self.kwargs = kwargs
        elif not hasattr(self, 'kwargs'):
            self.kwargs = None

    def get_raw(self, data, result=None):
        args = (
            () if self.args is None
            else self.args.get(data, result)
        )
        kwargs = (
            {} if self.kwargs is None
            else self.kwargs.get(data, result)
        )
        return self.init(*args, **kwargs)
