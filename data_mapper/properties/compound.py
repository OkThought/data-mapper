from data_mapper.result import MapResult
from data_mapper.properties.property import Property


class CompoundProperty(Property):
    _default_options = dict(
        sources=[[]],
        lazy=False,
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
        self.props_map = props_map
        super().__init__(sources_it=sources, **_options)

    def configure_sources(self):
        for key, prop in self.props_map.items():
            self.configure_source(prop, key)

    def configure_source(self, prop, key=None, *args, **kwargs):
        assert key is not None
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

    def __repr__(self):
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
