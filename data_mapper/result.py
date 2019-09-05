from typing import Iterator, Tuple, Any


class MapResult:
    def __init__(
            self,
            props_map,
            data,
            lazy: bool = True,
            result=None,
    ):
        self.props_map = props_map
        self.data = data
        self.cache = {}
        self._result = result
        if not lazy:
            self.evaluate()

    def evaluate(self):
        for _ in self:
            pass

    def keys(self):
        return self.props_map.keys()

    @property
    def result(self):
        return self if self._result is None else self._result

    def __iter__(self) -> Iterator[Tuple[Any, Any]]:
        return (
            (key, self[key])
            for key in self.props_map.keys()
        )

    def __getitem__(self, item):
        try:
            value = self.cache[item]
        except KeyError:
            prop = self.props_map[item]
            value = prop.get(self.data, self.result)
            self.cache[item] = value
        return value

    def get(self, key, default=None):
        try:
            value = self[key]
        except KeyError:
            value = default
        return value

    def __eq__(self, right):
        left = dict(self)
        if isinstance(right, MapResult):
            right = dict(right)
        return left == right
