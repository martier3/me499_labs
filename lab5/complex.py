#!/usr/bin/env python

class Complex:

    def __init__(self, re=float(0), im=float(0)):
        self.re = float(re)
        self.im = float(im)


    def __add__(self, other):
        if isinstance(other, (float,int)):
            return Complex(self.re + other, self.im)
        else:
            return Complex(self.re + other.re, self.im + other.im)


    def __radd__(self, other):
        return self.__add__(other)


    def __sub__(self, other):
        if isinstance(other, (float,int)):
            return Complex(self.re - other, self.im)
        else:
            return Complex(self.re - other.re, self.im - other.im)


    def __rsub__(self, other):
        return self.__sub__(other)


    def __mul__(self, other):
        if isinstance(other, (float,int)):
            return Complex(self.re * other, self.im * other)
        else:
            return Complex(self.re * other.re - self.im * other.im,
                       self.im * other.re + self.re * other.im)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (float, int)):
            r = float(other ** 2)
            return Complex((self.re * other +self.im * 0) / r,
                           (self.im * other -self.re * 0) / r)
        else:
            r = float(other.re ** 2 + other.im ** 2)
            return Complex((self.re * other.re + self.im * other.im) / r,
                           (self.im * other.re - self.re * other.im) / r)

    def __rtruediv__(self, other):
        return self.__truediv__(other)


    def __str__(self):
        if self.im < 0:
            total = '(%s - %si)' % (self.re, abs(self.im))
            return total
        else:
            total = '(%s + %si)' % (self.re, self.im)
            return total
