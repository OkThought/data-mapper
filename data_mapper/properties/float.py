from typing import Optional

from data_mapper.properties.property import Property


class FloatProperty(Property):
    def get_raw(self, data, result=None) -> Optional[float]:
        value = super().get_raw(data, result)
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                value = self.value_if_not_found()
        return value
