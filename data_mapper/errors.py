class PropertyNotResolved(LookupError):
    def __init__(self, prop):
        self.prop = prop
        super().__init__(str(prop))


PropertyNotFound = PropertyNotResolved  # backwards compatibility


class ValidationError(ValueError):
    pass
