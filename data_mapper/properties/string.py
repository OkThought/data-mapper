from data_mapper.properties.property import Property


class StringProperty(Property):
    def eval_not_none(self, value, **context):
        value = super().eval_not_none(value, **context)
        return str(value)
