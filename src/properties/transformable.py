from abc import ABC, abstractmethod
from typing import Iterable, Callable

from src.properties.abstract import AbstractProperty
from src.utils import NOT_SET


class TransformableProperty(AbstractProperty, ABC):
    transforms = []

    def __init__(self, transforms: Iterable[Callable[[str], str]] = NOT_SET):
        if transforms is not NOT_SET:
            self.transforms = transforms

    @abstractmethod
    def get_raw(self, data, result=None):
        pass

    def get(self, data: dict, result=None):
        value = self.get_raw(data, result)
        self.validate_raw(value)
        value = self.transform(value)
        self.validate(value)
        return value

    def transform(self, value):
        for transform in self.get_transforms():
            value = transform(value)
        return value

    def get_transforms(self):
        return self.transforms
