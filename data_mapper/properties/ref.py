from data_mapper.properties import Property


class PropertyRef(Property):
    def __init__(self, *sources, sources_it=None, **kwargs):
        if len(sources) == 1 and hasattr(sources[0], '__iter__') \
                and not isinstance(sources[0], str):
            # backwards compatibility
            sources_it, sources = sources[0], ()
        super().__init__(*sources, sources_it=sources_it, **kwargs)

    def get(self, data, result=None):
        assert result is not None, \
            'result is none, probably property has no parent. ' \
            f'You can only use {self.__class__.__name__} inside of other ' \
            'property that has its own result (e.g. CompoundProperty). ' \
            'Or you can pass your own object as a result.'
        value = result
        sources = self.get_sources()
        assert sources, 'no sources, must be set at some point'
        for sub_source in sources:
            value = self.get_value(value, sub_source)
        return value
