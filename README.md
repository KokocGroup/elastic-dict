# ElasticDict
Subclass of dict for preparing large nested structures

Motivation for creating this package was fatigue of preparing data for django templates.
It is very boring to create nested dictionaries with enomorous quantity of brackets and quotes.

Significant but not the only feature is automatic creation of nestes subdictionaries once acccessing them.

I wish using dot-notation for both creating and accessing:
```python
data = ElasticDict()
data.divisions.sales.persons[123].name = 'Alex'
print data.divisions.sales.persons[123].name
```

Instead of usual way of creating nested arrays:
```python
# creating
data = {}
data.setdefault('divisions',{}).setdefault('sales',{}).setdefault('persons',{}).setdefault(123, {})['name'] = 'Alex'
# accessing
print data['divisions']['sales']['persons'][123]['name']
```

## Installation
```sh
pip install elastic-dict
```

## Usage

### Examples
```
>>> from elasticdict import ElasticDict
>>> a = ElasticDict()
>>> a.x = 3
>>> print a
{'x': 3}

>>> a.y.z = (1,2,3,)
>>> print a
{'y': {'z': (1, 2, 3)}, 'x': 3}

Any address to non-existed keys will automaticall create it with value of type ElasticDict.
So it could be used recursively.
>>> print a.b.c.d
{}
>>> print a
{'y': {'z': (1, 2, 3)}, 'x': 3, 'b': {'c': {'d': {}}}}

Following expression violates python syntax:
>>> print a.01234
SyntaxError: invalid syntax
But such elements can still be addressed by usual way using brackets.

>>> a['01234'] = 7
>>> print a
{'y': {'z': (1, 2, 3)}, 'x': 3, 'b': {'c': {'d': {}}}, '01234': 7}

It is possible to mix both ways of addressing for your taste.
>>> a['qwer'].d.x.e[234] = 14
>>> print a
{'qwer': {'d': {'x': {'e': {234: 14}}}}}
>>> print a.qwer.d.x.e[234]
14
```
