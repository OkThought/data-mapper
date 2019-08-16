from data_mapper.mappers.result import MapResult
from data_mapper.properties.property import Property


class CompoundProperty(Property):
    _default_options = dict(
        sources=[[]],
        lazy=True,
    )

    def __init__(
            self,
            _options: dict = None,
            **props_map,
    ):
        if _options is None:
            _options = {}
        _options = {**self._default_options, **_options}
        self.lazy = _options.pop('lazy')
        sources = _options.pop('sources')
        super().__init__(sources_it=sources, **_options)
        self.props_map = props_map
        self.configure_props_map(props_map)

    def configure_props_map(self, props_map):
        for key, prop in props_map.items():
            self.configure_prop_sources(prop, key)

    @staticmethod
    def configure_prop_sources(prop, key):
        if getattr(prop, 'sources', 0) is None:
            prop.sources = [key]

    def get_raw(self, data, result=None):
        result = MapResult(
            self.props_map,
            data=super().get_raw(data, result),
            lazy=self.lazy,
        )
        return result
