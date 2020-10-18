print("Введите целое положительное число")
number = int(input())
numeral_max = number % 10
while number // 10 != 0:
    max_new = number % 10
    if max_new > numeral_max:
        numeral_max = max_new
    number = number // 10

if number > numeral_max:
    numeral_max = number

print(f'Максимальная цифра {numeral_max}')



