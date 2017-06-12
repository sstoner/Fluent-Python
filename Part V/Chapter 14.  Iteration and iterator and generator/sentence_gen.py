import re
import reprlib

RE_WORD = re.compile("\w+")

class Sentence:

    def __init__(self,text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        #return

s = Sentence("hello vance night nginx")


def gen_ABC():
    print("start")
    yield "A"
    print("continue")
    yield "B"
    print("end")
    yield "C"

for i in gen_ABC():
    print("--->",i)