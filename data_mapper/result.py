from typing import Iterator, Any, Mapping


class MapResult(Mapping):
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

    def __len__(self) -> int:
        return len(self.props_map)

    def evaluate(self):
        for _ in self:
            pass

    def keys(self):
        return self.props_map.keys()

    def items(self):
        return ((k, self[k]) for k in self.keys())

    @property
    def result(self):
        return self if self._result is None else self._result

    def __iter__(self) -> Iterator[Any]:
        return iter(self.keys())

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
