from typing import Optional

from data_mapper.properties.property import Property


class IntegerProperty(Property):
    def get_raw(self, data, result=None) -> Optional[int]:
        value = super().get_raw(data, result)
        if value is not None:
            value = int(value)
        return value
