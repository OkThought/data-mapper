from typing import Optional

from data_mapper.properties.property import Property


class IntegerProperty(Property):
    def get_raw(self, data, result=None) -> Optional[int]:
        value = super().get_raw(data, result)
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                value = self.value_if_not_found()
        return value
