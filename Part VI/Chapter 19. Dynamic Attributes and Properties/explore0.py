from collections import abc
import json
import  keyword

class FrozenJSON:

    def __init__(self,mapping):
        self.__data = {}
        for key,value in mapping.items():
            if keyword.iskeyword(key):
                key+='_'
            self.__data[key] =value

    def __getattr__(self, item):
        if hasattr(self.__data,item):
            return getattr(self.__data,item)
        else:
            return FrozenJSON.build(self.__data[item])

    @classmethod
    def build(cls,obj):
        if isinstance(obj,abc.Mapping):
            return cls(obj)
        elif isinstance(obj,abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


with open("osconfeed.json") as fp:
    raw_feed = json.load(fp)

print(raw_feed)
feed = FrozenJSON(raw_feed)
print(feed.Schedule)