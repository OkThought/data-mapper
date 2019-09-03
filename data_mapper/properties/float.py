from data_mapper.properties.property import Property


class FloatProperty(Property):
    def eval_not_none(self, value, **context):
        return float(super().eval_not_none(value, **context))
