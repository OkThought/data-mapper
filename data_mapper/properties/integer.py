from data_mapper.properties.property import Property


class IntegerProperty(Property):
    def eval_not_none(self, value, **context):
        return int(super().eval_not_none(value, **context))
