from typing import Iterable

from src.properties.property import Property
from src.utils import NOT_SET


class ListProperty(Property):
    allowed_types = None

    def __init__(self, allowed_types: Iterable[type] = NOT_SET, **kwargs):
        super().__init__(**kwargs)

        if allowed_types is not NOT_SET:
            self.allowed_types = allowed_types

    def transform(self, value):
        return super().transform(list(value))
