class MyZeroDivisionException(Exception):
    def __init__(self, message):
        self.message = message


try:
    dividend = int(input("Введите делимое: "))
    divisor = int(input("Введите делитель: "))
    if divisor == 0:
        raise MyZeroDivisionException("Нельзя делить на ноль")
    print(dividend / divisor)
except MyZeroDivisionException as ex:
    print(ex.message)