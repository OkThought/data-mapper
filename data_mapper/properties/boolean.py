from data_mapper.properties.property import Property


class BooleanProperty(Property):
    def __init__(
            self,
            *args,
            bool_fn=None,
            true_values=None,
            false_values=None,
            **kwargs,
    ):
        assert len(tuple(filter(None, (
            bool_fn, true_values, false_values
        )))) <= 1, 'arguments `bool_fn`, `true_values` and `false_values` ' \
                   'are exclusive'

        super().__init__(*args, **kwargs)

        if not hasattr(self, 'bool_fn'):
            if bool_fn is not None:
                self.bool_fn = bool_fn
            elif true_values is not None:
                self.bool_fn = lambda v: v in true_values
            elif false_values is not None:
                self.bool_fn = lambda v: v not in false_values
            else:
                self.bool_fn = bool

    def get(self, data: dict, result=None):
        return self.bool_fn(super().get(data, result))
