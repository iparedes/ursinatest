class vector3:

    def __init__(self,a):
        self._data=a

    @property
    def x(self):
        return self._data[0]

    @x.setter
    def x(self,v):
        self._data[0]=v

    @property
    def y(self):
        return self._data[1]

    @y.setter
    def y(self,v):
        self._data[1]=v

    @property
    def z(self):
        return self._data[2]

    @z.setter
    def z(self,v):
        self._data[2]=v

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"

    def __add__(self, other):
        t=[x+y for x,y in zip(self._data,other._data)]
        return t

    def __truediv__(self, other):
        if isinstance(other,(int,float)):
            other=vector3([other,other,other])
        t=[x/y for x,y in zip(self._data, other._data)]
        return t