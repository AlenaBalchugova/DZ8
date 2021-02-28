class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber((self.a * other.a - (self.b * other.b)), (self.b * other.a + self.a * other.b))

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


first_number = ComplexNumber(7, 3)
second_number = ComplexNumber(5, -8)
print(first_number)
print(second_number)
print(f'Сумма комплексных чисел равна')
print(first_number + second_number)
print(f'Произведение равно')
print(first_number * second_number)