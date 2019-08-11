from typing import Iterator, Tuple, Any


class MapResult:
    def __init__(self, props_map, data, lazy: bool = True):
        self.props_map = props_map
        self.data = data
        self.result = {}
        if not lazy:
            self.evaluate()

    def evaluate(self):
        for _ in self:
            pass

    def keys(self):
        return self.props_map.keys()

    def __iter__(self) -> Iterator[Tuple[Any, Any]]:
        return (
            (key, self[key])
            for key in self.props_map.keys()
        )

    def __getitem__(self, item):
        try:
            value = self.result[item]
        except KeyError:
            value = self.props_map[item].get(self.data, self)
            self.result[item] = value
        return value

    def __eq__(self, right):
        left = dict(self)
        if isinstance(right, MapResult):
            right = dict(right)
        return left == right
