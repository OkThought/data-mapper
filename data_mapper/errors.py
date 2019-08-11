from typing import Iterable


class PropertyNotFound(ValueError):
    def __init__(self, sources: Iterable):
        super().__init__(f'Property not found in sources: {sources}')


class ValidationError(ValueError):
    pass
