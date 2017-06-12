import re
import reprlib

RE_WORD = re.compile("\w+")

class Sentence:

    def __init__(self,text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, item):      #self.__getitem__(item)
        #return self.words[item]
        try:
            return self.words[item]
        except Exception as e:
            return ("hello,you're wrong! \n", e)

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)


sentence = Sentence("hellonihao")
print(sentence[7])