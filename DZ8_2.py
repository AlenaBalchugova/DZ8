class MyZeroDivisionError(Exception):
    def __init__(self, msg):
        self.msg = msg


def division(a, b):
    if b == 0:
        raise MyZeroDivisionError('Делить на ноль нельзя')

    return a/b


def main():
    print('Деление')
    a = float(input('Ведите делимое: '))
    b = float(input('Введите делитель b: '))
    try:
        print('Результат деления', division(a, b))
    except MyZeroDivisionError as e:
        print(e)


main()