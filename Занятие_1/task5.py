print("Введите значение выручки: ")
proc = int(input())
print("Введите значение издержек: ")
costs = int(input())
if proc > costs:
    print('Прибыль')
    profit = (proc - costs) / proc
    print("Рентабельность: ", "{:.2f}".format(profit))
    print("Введите количество сотрудников: ")
    number = int(input())
    profit_emp = (proc - costs) / number
    print('Прибыль на одного сотрудника: ', "{:.2f}".format(profit_emp))
else:
    print("Убыток")
