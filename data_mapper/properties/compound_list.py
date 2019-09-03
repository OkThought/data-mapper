from data_mapper.properties.functional import Operation


class CompoundListProperty(Operation):
    func = list

    def __init__(
            self,
            *args,
            skip_none: bool = False,
            **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.skip_none = skip_none

    def eval_not_none(self, value, **context):
        value = super().eval_not_none(value, **context)
        if self.skip_none:
            value = [i for i in value if i is not None]
        return value
