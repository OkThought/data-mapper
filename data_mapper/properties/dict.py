from data_mapper.properties.property import Property


class DictProperty(Property):
    def get(self, data: dict, result=None):
        return dict(super().get(data, result))
