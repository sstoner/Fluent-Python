from collections import abc
from keyword import iskeyword
import  json
class FrozenJSON:

    def __new__(cls, arg):
        if isinstance(arg,abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg,abc.MutableSequence):
            return [ cls(item) for item in arg]
        else:
            return arg

    def __init__(self,mapping):
        self.__data = {}
        for key,value in mapping.items():
            if iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, item):
        if hasattr(self.__data,item):
            return getattr(self.__data,item)
        else:
            return FrozenJSON(self.__data[item])

with open("osconfeed.json") as fp:
    raw_feed = json.load(fp)

feed = FrozenJSON(raw_feed)
print(feed.items())
print(feed.Schedule.events)

