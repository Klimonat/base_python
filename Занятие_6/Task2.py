class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def count(self):
        weight = (self._length * self._width * 25 * 5) / 1000
        print(weight)

width = int(input('Введите ширину: '))
length = int(input('Введите длину: '))
find_weight = Road(width, length)
find_weight.count()