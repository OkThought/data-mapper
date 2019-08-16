from data_mapper.properties.property import Property


class IntegerProperty(Property):
    def get_raw(self, data, result=None):
        return int(super().get_raw(data, result))
