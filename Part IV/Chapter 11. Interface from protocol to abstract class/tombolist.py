from random import randrange
from tombola import Tombola

@Tombola.register
class TomboList(list):

    def pick(self):
        if self:
            pos = randrange(len(self))
            return self.pop(pos)
        else:
            raise LookupError("pop from empty TomboList")

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))

#Tombola.register(TomboList)

asd = TomboList()

asd.load([1,2,3])
print(asd)
asd.load([7,8,9])
print(asd)
print(asd.inspect())
for i in range(10):
    print(asd.pick())
