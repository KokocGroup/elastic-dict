# ElasticDict
Subclass of dict for preparing large nested structures

Motivation for creating this package was fatigue of preparing data for django templates.
It is very boring to create nested dictionaries with enomorous quantity of brackets and quotes.

Instead of usual way of creating nested arrays:
```python
# creating
data.setdefault('divisions',{}).setdefault('sales',{}).setdefault('persons',{}).setdefault(123, {})['name'] = 'Alex'
# accessing
print data['divisions']['sales']['persons'][123]['name']
```

I wish using dot-notation for both creating and accessing:
```python
data.divisions.sales.persons[123].name = 'Alex'
print data.divisions.sales.persons[123].name
```

## Installation
```sh
pip install elastic-dict
```

## Usage
```python
from elasticdict import ElasticDict
a = ElasticDict()
a.b.c.d.e = 3
print a
```
