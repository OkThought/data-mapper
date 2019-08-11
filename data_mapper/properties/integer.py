from data_mapper.properties.property import Property


class IntegerProperty(Property):
    def get(self, data: dict, result=None):
        return int(super().get(data, result))
