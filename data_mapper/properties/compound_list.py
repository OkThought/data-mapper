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

    def get(self, data, result=None):
        value = super().get(data, result)
        if self.skip_none:
            value = [i for i in value if i is not None]
        return value
