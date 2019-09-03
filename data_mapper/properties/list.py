from data_mapper.properties.property import Property


class ListProperty(Property):
    def eval_not_none(self, value, **context):
        return list(super().eval_not_none(value, **context))
