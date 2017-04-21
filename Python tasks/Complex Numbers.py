import sys


class ComplexNumber:
    def __init__(self, real=0., imaginary=0.):
        self.real = float(real)
        self.imaginary = float(imaginary)

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary +
                             other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary -
                             other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary *
                             other.imaginary,
                             self.real * other.imaginary + self.imaginary *
                             other.real)

    def __truediv__(self, other):
        return ComplexNumber((self.real * other.real + self.imaginary *
                              other.imaginary) /
                             (other.real ** 2 + other.imaginary ** 2),
                             (self.imaginary * other.real - self.real *
                              other.imaginary) /
                             (other.real ** 2 + other.imaginary ** 2))

    def _sign_s(self):
        if self.imaginary >= 0.:
            return '+'
        else:
            return '-'

    def __str__(self):
        if self.real != 0. and self.imaginary != 0.:
            return "{0:.2f}".format(round(self.real, 2)) + ' ' \
                   + self._sign_s() + ' ' + \
                   "{0:.2f}".format(round(abs(self.imaginary), 2)) + 'i'
        elif self.real == 0. and self.imaginary != 0.:
            return "{0:.2f}".format(round(self.imaginary), 2) + 'i'
        else:
            return "{0:.2f}".format(round(self.real, 2))


# def main():
#   for line in sys.stdin.readlines():
#      print(eval(line.strip()))

if __name__ == "__main__":
    for line in sys.stdin.readlines():
        print(eval(line.strip()))
