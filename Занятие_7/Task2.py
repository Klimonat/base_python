from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def count(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size > 0:
            self.__size = size
        else:
            self.__size = -size

    def count(self):
        return self.__size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, size):
        if height > 0:
            self.__height = height
        else:
            self.__height = -height

    def count(self):
        return 2 * self.__height + 0.3

print('Введите размер для пальто: ')
size = float(input())
print('Введите рост для костюма: ')
height = float(input())
a = Coat(size)
print("Для пальто потребуется: ", "%.3f" % a.count())
b = Suit(height)
print("Для костюма потребуется: ", "%.3f" % b.count())

print("Суммарно потребуется ткани:  ", "%.3f" % (a.count() + b.count()))