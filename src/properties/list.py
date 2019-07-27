from typing import Iterable

from src.properties.property import Property
from src.utils import NOT_SET


class ListProperty(Property):
    allowed_types = None

    def __init__(self, allowed_types: Iterable[type] = NOT_SET, **kwargs):
        super().__init__(**kwargs)

        if allowed_types is not NOT_SET:
            self.allowed_types = allowed_types

    def get_raw(self, src: dict):
        return super().get_raw(src)

    def transform(self, value: str):
        return super().transform(list(value))
