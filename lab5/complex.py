#!/usr/bin/env python

class Complex:

    def __init__(self, re=float(0), im=float(0)):
        self.re = float(re)
        self.im = float(im)

    def __str__(self):
        if self.im < 0:
            return '(%s - %si)' % (self.re, self.im)
        else:
            return '(%s + %si)' % (self.re, self.im)


print(Complex(-3, 2))
print(Complex())
print(Complex(3.4, -2.1))