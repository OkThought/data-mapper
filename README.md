# data-mapper
A declarative data mapper

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

### Different property naming

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
