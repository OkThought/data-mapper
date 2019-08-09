from typing import Tuple

from src.errors import ValidationError
from src.properties.property import Property
from src.utils import NOT_SET


class ListProperty(Property):
    def __init__(self, allowed_types: Tuple[type] = NOT_SET, **kwargs):
        super().__init__(**kwargs)
        self.allowed_types = allowed_types

    def get_raw(self, data: dict, result=None):
        return list(super().get_raw(data, result))

    def transform(self, value):
        return super().transform(value)

    def validate_raw(self, value):
        super().validate_raw(value)

        if self.allowed_types is NOT_SET:
            return

        for elem in value:
            if not isinstance(elem, self.allowed_types):
                raise ValidationError(
                    f'Wrong element type: {type(elem)}. '
                    f'Types allowed: {self.allowed_types}')
