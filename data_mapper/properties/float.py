from data_mapper.properties.property import Property


class FloatProperty(Property):
    def get(self, data: dict, result=None):
        return float(super().get(data, result))
