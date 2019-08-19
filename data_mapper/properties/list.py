from typing import Tuple, Optional

from data_mapper.errors import ValidationError
from data_mapper.properties.property import Property
from data_mapper.utils import NOT_SET


class ListProperty(Property):
    def __init__(self, *args, allowed_types: Tuple[type] = NOT_SET, **kwargs):
        super().__init__(*args, **kwargs)
        self.allowed_types = allowed_types

    def get_raw(self, data: dict, result=None) -> Optional[list]:
        value = super().get_raw(data, result)
        if value is not None:
            value = list(value)
        return value

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
