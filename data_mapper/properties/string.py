from data_mapper.properties.property import Property


class StringProperty(Property):
    def get_raw(self, data, result=None):
        value = super().get_raw(data, result)
        if value is not None:
            value = str(value)
        return value
