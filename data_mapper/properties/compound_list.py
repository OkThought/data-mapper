from data_mapper.errors import ValidationError
from data_mapper.properties.operations import Operation


class CompoundListProperty(Operation):
    func = list

    def __init__(
            self,
            *args,
            allowed_sizes=None,
            skip_none: bool = False,
            **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.allowed_sizes = allowed_sizes
        self.skip_none = skip_none

    def get_raw(self, data, result=None):
        value = super().get_raw(data, result)
        if self.skip_none:
            value = [i for i in value if i is not None]
        return value

    def validate_raw(self, value):
        if self.allowed_sizes is not None:
            size = len(value)
            if size not in self.allowed_sizes:
                raise ValidationError(f'Wrong size: {size}')
