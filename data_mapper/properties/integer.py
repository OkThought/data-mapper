from data_mapper.properties.property import Property


class IntegerProperty(Property):
    get_value_exc_default = Property.get_value_exc_default + (ValueError,)

    def eval_not_none(self, value, **context):
        return int(super().eval_not_none(value, **context))
