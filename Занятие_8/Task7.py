class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f'{self.real} + {self.imaginary}i'

    def __add__(self, complex_number):
        return ComplexNumber(self.real + complex_number.real, self.imaginary + complex_number.imaginary)

    def __mul__(self, complex_number):
        real = self.real * complex_number.real - self.imaginary * complex_number.imaginary
        imaginary = self.real * complex_number.imaginary + self.imaginary * complex_number.real
        return ComplexNumber(real, imaginary)


number1 = ComplexNumber(1, 5)
print(number1)
number2 = ComplexNumber(2, 3)
print(number2)
add = number1 + number2
print(f'add: {add}')
mult = number1 * number2
print(f'mult: {mult}')


