# data-mapper
A declarative data mapper

![PyPI](https://img.shields.io/pypi/v/data-mapper?style=for-the-badge)
![Travis (.org) branch](https://img.shields.io/travis/OkThought/data-mapper/master?logo=travis&style=for-the-badge)

## Description

Most projects work with different representations of the same data.
The code that is written every time to morph data between its representations
is mostly very repetitive. More over, it is always a deposit of bugs and issues
which requires a developer or tester to unit-test it.

This package is an attempt to solve these problems... well, at least the most
common ones.

And to make a developer job easier it is primarily designed to be used
in declarative fashion: describe what you want and get it right after.

## Use Cases and Features

Here are examples of the most common use-cases and features: 

### Different Naming Schemes

This mapper looks for properties `first_name` and `last_name` in the data.
For property `first_name` it tries to resolve it by the first key 
`'first_name'`, if not found it tries the second key `'name'`.
The similar process goes for property `last_name`.

```python
from data_mapper.mappers import Mapper
from data_mapper.properties import Property

class PersonMapper(Mapper):
    first_name = Property('first_name', 'name')
    last_name = Property('last_name', 'surname')

mapper = PersonMapper()

assert mapper.get({
    'first_name': 'Ivan', 
    'surname': 'Bogush',
}) == {
    'first_name': 'Ivan', 
    'last_name': 'Bogush',
}

assert mapper.get({
    'name': 'Ivan', 
    'surname': 'Bogush',
}) == {
    'first_name': 'Ivan', 
    'last_name': 'Bogush',
}
```

This use-case has a story :)
> It was the first issue I wanted to solve in my other project. I had different 
naming schemes in different data sources, and in my databases. All of them used 
different names for product categories: 'categories', 'category', 'categoryId'.
I found it very boring to write repeatable code to convert the same data.

### Arbitrary functions on resolved values

#### Full Name String Construction
This one resolves properties `first_name`, `middle_name` [optionally] and 
`last_name` and combines them into a single string — `full_name`.

```python
from data_mapper.shortcuts import F, Str, L

full_name = F(
    ' '.join,
    L(
        Str('first_name'),
        Str('middle_name', required=False),
        Str('last_name'),
        skip_none=True,
    ),
)

assert 'Anton Pavlovich Chekhov' == full_name.get(dict(
    first_name='Anton',
    middle_name='Pavlovich',
    last_name='Chekhov',
))

assert 'Anton Chekhov' == full_name.get(dict(
    first_name='Anton',
    last_name='Chekhov',
))
```

### Object mapping

#### Dict to *Object*

Let's assume we have a class `Person`:
```python
class Person:
    def __init__(
            self,
            id_: int,
            first_name: str,
            last_name: str,
            middle_name: str = None,
    ):
        self.id = id_
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
```

A mapper from dict with corresponding keys to an instance of class `Person` 
could be defined by subclassing `ObjectMapper`:

```python
from data_mapper.mappers.object import ObjectMapper
from data_mapper.properties import (
    CompoundProperty, CompoundListProperty, IntegerProperty, StringProperty,
)


class PersonMapper(ObjectMapper):
    init = Person
    args = CompoundListProperty(
        IntegerProperty('id'),
        StringProperty('first_name'),
        StringProperty('last_name'),
    )
    kwargs = CompoundProperty(
        middle_name=StringProperty(required=False),
    )

first, middle, last = 'Iosif Aleksandrovich Brodsky'.split()
person = PersonMapper().get(dict(
    id=1940,
    first_name=first,
    middle_name=middle,
    last_name=last,
))

assert isinstance(person, Person)
assert person.id == 1940
assert person.first_name == first
assert person.middle_name == middle
assert person.last_name == last
```

Exactly the same can be done by instantiating the `ObjectMapper`:

```python
from data_mapper.mappers.object import ObjectMapper
from data_mapper.properties import (
    CompoundProperty, CompoundListProperty, IntegerProperty, StringProperty,
)


mapper = ObjectMapper(
    init=Person,
    args=CompoundListProperty(
        IntegerProperty('id'),
        StringProperty('first_name'),
        StringProperty('last_name'),
    ),
    kwargs=CompoundProperty(
        middle_name=StringProperty(required=False),
    ),
)

first, middle, last = 'Iosif Aleksandrovich Brodsky'.split()
person = mapper.get(dict(
    id=1940,
    first_name=first,
    middle_name=middle,
    last_name=last,
))

assert isinstance(person, Person)
assert person.id == 1940
assert person.first_name == first
assert person.middle_name == middle
assert person.last_name == last
```
