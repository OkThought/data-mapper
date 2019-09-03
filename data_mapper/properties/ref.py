from data_mapper.properties.abstract import AbstractProperty


class PropertyRef(AbstractProperty):
    def __init__(self, *sources, sources_it=None):
        assert not sources or sources_it is None

        if not sources:
            sources = sources_it
        elif len(sources) == 1 and hasattr(sources[0], '__iter__') \
                and not isinstance(sources[0], str):
            # backwards compatibility
            sources = sources[0]

        assert sources
        self.sources = sources

    def get(self, data, result=None):
        value = result
        for sub_source in self.sources:
            value = value[sub_source]
        return value
