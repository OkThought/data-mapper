from typing import Iterable, Callable

from src.errors import PropertyNotFound
from src.utils import NOT_SET


class Property:
    transforms = []
    required = True
    default = NOT_SET
    sources = None

    def __init__(
            self,
            sources: Iterable = NOT_SET,
            default: str = NOT_SET,
            required: bool = NOT_SET,
            transforms: Iterable[Callable[[str], str]] = NOT_SET,
    ):
        if sources is not NOT_SET:
            self.sources = sources

        assert default is NOT_SET or not required

        if default is not NOT_SET:
            self.default = default
        if self.required is not NOT_SET:
            self.required = required
        if transforms is not NOT_SET:
            self.transforms = transforms

    def get(self, data: dict, alt_sources: Iterable = None):
        sources = self.sources if alt_sources is None else alt_sources
        assert sources, \
            'At least one source must be defined either through argument ' \
            '`alt_sources` or field `sources`'
        value = self.get_raw(data, sources)
        value = self.transform(value)
        return value

    def get_raw(self, src: dict, sources: Iterable):
        for source in sources:
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

    def transform(self, value: str):
        for transform in self.get_transforms():
            value = transform(value)
        return value

    def get_transforms(self):
        return self.transforms
