class PropertyNotResolved(LookupError):
    def __init__(self, prop, sub_errors):
        self.prop = prop
        if sub_errors:
            sub_errors_str = ': \n' + ('\n'.join(map(str, sub_errors)))
        else:
            sub_errors_str = ''
        super().__init__(f'{prop}{sub_errors_str}')


PropertyNotFound = PropertyNotResolved  # backwards compatibility


class ValidationError(ValueError):
    pass
