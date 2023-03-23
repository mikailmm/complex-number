from numbers import Number


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b == 1:
            return f'{self.a}+i'
        if self.b >= 0:
            return f'{self.a}+{self.b}i'
        return f'{self.a}{self.b}i'

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.a + other.a, self.b + other.b)
        elif isinstance(other, Number):
            return Complex(self.a + other, self.b)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.a - other.a, self.b - other.b)
        elif isinstance(other, Number):
            return Complex(self.a - other, self.b)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, Complex):
            return Complex(other.a - self.a, self.b - other.b)
        elif isinstance(other, Number):
            return Complex(other - self.a, -self.b)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex((self.a*other.a) - (self.b*other.b),
                           (self.a*other.b) + (self.b*other.a))
        elif isinstance(other, Number):
            return Complex(self.a*other, self.b*other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, Complex):
            return Complex((self.b*other.b) - (self.a*other.a),
                           (self.b*other.a) + (self.a*other.b))
        elif isinstance(other, Number):
            return Complex(self.a*other, self.b*other)
        else:
            return NotImplemented

    def __reciprocal(self):
        a = (self.a) / (self.a*self.a + self.b*self.b)
        b = -(self.b) / (self.a*self.a + self.b*self.b)
        return Complex(a, b)

    def __truediv__(self, other):
        if isinstance(other, Complex):
            return self * other.__reciprocal()
        elif isinstance(other, Number):
            return Complex(self.a/other, self.b/other)
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, Number):
            return other * self.__reciprocal()
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Complex):
            return (self.a == other.a) and (self.b == other.b)
        elif isinstance(other, Number):
            return (self.a == other) and (self.b == 0)
        else:
            return NotImplemented

    def __pow__(self, other):
        val = 1
        if isinstance(other, Number):
            for i in range(other):
                val = val * self
            return val
        else:
            return NotImplemented
