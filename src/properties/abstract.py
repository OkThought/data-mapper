from abc import abstractmethod


class AbstractProperty:
    @abstractmethod
    def get(self, data, result=None):
        pass

    def validate_raw(self, value):
        return

    def validate(self, value):
        return
