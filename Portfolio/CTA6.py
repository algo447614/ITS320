#------------------------------------------------------------------------
# Program Name: ITS320_CTA6_Option1.py
# Author: Aliciana Gondick
# Date: Sept. 25, 2023
# Program Objective: produce the sum, difference, product, dividend,
# and modulus operand of two complex numbers
#------------------------------------------------------------------------
# Pseudocode:
#   1. User will input complex numbers
#   2. Program will create class for numbers as object
#   3. Program will produce sum, difference, product, dividend, and mod. op.
#------------------------------------------------------------------------
# Program Inputs: Complex numbers
# Program Outputs: Mathematical operations of complex numbers
#------------------------------------------------------------------------

print("This will produce the following input for two complex numbers: \nC + D\nC - D\nC * D\nC / D\nmod(C)\nmod(D)")
print("Please input your numbers")

import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real,imaginary)

    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return Complex(real, imaginary)

    def __mul__(self, no):
        real = self.real * no.real
        imaginary = self.imaginary * no.imaginary
        return Complex(real, imaginary)

    def __truediv__(self, no):
        real = self.real / no.real
        imaginary = self.imaginary / no.imaginary
        return Complex(real, imaginary)

    def mod(self):
        real = (self.real**2 + self.imaginary**2)**0.5
        return Complex(real, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

# put this code in a main method
C = map(float, input().split())
D = map(float, input().split())
x = Complex(*C)
y = Complex(*D)
print ('\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]))) 
