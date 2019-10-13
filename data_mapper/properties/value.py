from data_mapper.properties import Property


class Value(Property):
    def __init__(self, value, **kwargs):
        self.value = value
        super().__init__(**kwargs)

    def get(self, data, result=None):
        return self.value

    def __repr__(self):
        return f'Value({repr(self.value)})'
