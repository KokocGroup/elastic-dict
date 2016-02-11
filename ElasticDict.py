class ElasticDict(dict):
    """Dict which could adjust to you current needs

    It eliminates neccessity of using brackets when filling a dictionary:
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

    """
    def __init__(self, *args, **kwargs):
        super(ElasticDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            if item in dir(dict):
                return getattr(self, item)
            value = self[item] = type(self)()
            return value

    def __getattr__(self, name):
        if name in dir(dict) or name.startswith('_') or name in ('trait_names', 'resolve_expression', 'prepare_database_save'):  # can not be accessed by dot
            raise AttributeError()
        else:
            value = self.__dict__[name] = type(self)()
            return value

    def get_as_dict(self):
        u"""
            Exports self as ordinary dict(), replacing recursively all instances of ElasticDict() to dict()
        :rtype: dict()
        """
        def convert(val):
            if isinstance(val, tuple):
                return tuple(convert(v) for v in val)
            elif isinstance(val, list):
                return [convert(v) for v in val]
            elif isinstance(val, (dict, ElasticDict)):
                return {k: convert(v) for k, v in val.iteritems()}
            else:
                return val

        return convert(self.__dict__)

    @staticmethod
    def create_from(value):
        u"""
            Create an instance of ElasticDict() where all nested dict()'s are replaced to ElasticDict()
        :rtype: ElasticDict (if value is dict()), else type(value)
        """
        def convert(val):
            if isinstance(val, tuple):
                return tuple(convert(v) for v in val)
            elif isinstance(val, list):
                return [convert(v) for v in val]
            elif isinstance(val, (dict, ElasticDict)):
                return ElasticDict({k: convert(v) for k, v in val.iteritems()})
            else:
                return val

        return convert(value)