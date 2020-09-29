class myClass1:
    def __init__(self):
        self._x = None

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def delX(self):
        del self._x

    x = property(getX, setX, delX, "I'm the 'x' property.")

c1 = myClass1()
print(c1.x)
c1.x = 2
print(c1.x)
del c1.x
try:
    print(c1.x)
except:
    print("c1.x deleted")


class Parrot:
    def __init__(self):
        self.__voltage = 100000

    @property
    def voltag(self):
        """Get the current voltage"""
        return self.__voltage

p1 = Parrot()
print(p1.voltag)


class myClass2:
    def __init__(self):
        self.__x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @x.deleter
    def x(self):
        del self._x

c2 = myClass2()
c2.x = 3
print(c2.x)
