from abc import abstractmethod


class AbstractProperty:
    @abstractmethod
    def get(self, data, result=None):
        pass
