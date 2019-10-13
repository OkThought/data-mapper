from data_mapper.properties import Property


class PropertyRef(Property):
    default_sources = []

    def __init__(self, source=None, *sources, **kwargs):
        if source is not None:
            sources = [source, *sources]
        super().__init__(*sources, **kwargs)

    def get(self, data, result=None):
        assert result is not None, \
            'result is none, probably property has no parent. ' \
            f'You can only use {self.__class__.__name__} inside of other ' \
            'property that has its own result (e.g. CompoundProperty). ' \
            'Or you can pass your own object as a result.'
        return super().get(result)

    def configure_source(self, source, *args, **kwargs):
        pass

    def configure_sources(self, *args, **kwargs):
        pass

    def get_value_default(self, d, k):
        return d[k]
