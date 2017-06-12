import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence: #可迭代对象

    def __init__(self,text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)

class SentenceIterator: #迭代器

    def __init__(self,words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except Exception as e:
            raise e #must raise, cannot return
        self.index += 1
        return word

    def __iter__(self):
        return self


s = Sentence("hell vance you are right!")
q = SentenceIterator([1,2,3,4,5,6,7])
a = iter(s)
print(next(a))
#对迭代器的调用
print(next(q))
print(next(s.__iter__()))