from vector2d_v0 import Vector2d
v = Vector2d(4,5)

#print(v.__dict__)
#output: {'_Vector2d__x': 4.0, '_Vector2d__y': 5.0}
#print(v._Vector2d__x)
#4.0

"""
protected attribute is named _ClassName__attrName
"""


class pro_Vector2d(Vector2d):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.__x = x
        self.__y = y
        self._z = z

    def printt(self):
        print("subclass:",self._Vector2d__x,self._Vector2d__y)

s = pro_Vector2d(5,6,7)
print(s._pro_Vector2d__x)
print(s._z)