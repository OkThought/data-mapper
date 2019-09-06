from data_mapper.result import MapResult
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
        self.configure_props(props_map)

    def configure_props(self, props_map):
        for key, prop in props_map.items():
            self.configure_prop(prop, key)

    def configure_prop(self, prop, key):
        prop.parent = self
        if getattr(prop, 'sources', 0) is None:
            prop.sources = [key]

    def eval_not_none(self, value, result=None, **context):
        result = MapResult(
            self.props_map,
            data=super().eval_not_none(value, result=result, **context),
            lazy=self.lazy,
            result=result,
        )
        return result

    def __str__(self):
        return f"""{
        self.__class__.__name__
        }({
        f"sources={self.sources}, " 
        if self.sources is not None 
           and self.sources != self._default_options['sources']
        else ''
        }{
        ', '.join(f'{k}={v}' for k, v in self.props_map.items())
        })"""
