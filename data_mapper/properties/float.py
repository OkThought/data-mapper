from typing import Optional

from data_mapper.properties.property import Property


class FloatProperty(Property):
    def get_raw(self, data, result=None) -> Optional[float]:
        value = super().get_raw(data, result)
        if value is not None:
            value = float(value)
        return value
