from src.properties.property import Property


class StringProperty(Property):
    def transform(self, value: str):
        return super().transform(str(value))
