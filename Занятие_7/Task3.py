class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, cell):
        return Cell(self.count + cell.count)

    def __sub__(self, cell):
        return Cell(self.count - cell.count)


    def __mul__(self, cell):
        return Cell(self.count * cell.count)

    def __truediv__(self, cell):
        return Cell(int(self.count / cell.count))

    def make_order(self, number):
        output_str = ''
        self.number = number
        for i in range(self.count):
            if (i + 1) % number == 0:
                output_str += '*\n'
            else:
                output_str += '*'
        print(output_str)

print("Введите количество ячеек первой клетки: ")
count = int(input())
print("Введите количество ячеек второй клетки: ")
count_new = int(input())
cell1 = Cell(count)
cell2 = Cell(count_new)
add_cell = cell1 + cell2
print("Сумма ячеек двух клеток: ", add_cell.count)
if count - count_new <= 0:
    print("Разность количества ячеек отрицательна или равна нулю")
else:
    sub_cell = cell1 - cell2
    print("Разность ячеек двух клеток: ", sub_cell.count)
mul_cell = cell1 * cell2
print("Произведение ячеек двух клеток: ", mul_cell.count)
truediv_cell = cell1 / cell2
print("Частное ячеек двух клеток: ", truediv_cell.count)
print("Введите количество ячеек в ряду: ")
number = int(input())
cell1.make_order(number)