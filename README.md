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

### Arbitrary operations on resolved values

#### Full Name String Construction
This one resolves properties `first_name`, `middle_name` [optionally] and 
`last_name` and combines them into a single string — `full_name`.

```python
from data_mapper.properties.operations import Operation
from data_mapper.properties.string import StringProperty

full_name = Operation(
    StringProperty('first_name'),
    StringProperty('middle_name', required=False),
    StringProperty('last_name'),
    func=lambda *args: ' '.join(filter(None, args)),
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
