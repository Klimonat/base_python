from sys import argv

name, production, rate, prize = argv
salary = int(production) * int(rate) + int(prize)
print(salary)