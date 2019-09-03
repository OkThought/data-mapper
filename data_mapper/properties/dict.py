from data_mapper.properties.property import Property


class DictProperty(Property):
    def eval_not_none(self, value, **context):
        return dict(super().eval_not_none(value, **context))
