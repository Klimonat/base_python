class ListException(Exception):
    def __init__(self, message):
        self.message = message

list = []
elem = input("Введите элемент списка: ")
while elem != "stop":
    try:
        if elem.isnumeric():
            list.append(elem)
        else:
            raise ListException("Введено не число. Чтобы закончить, введите stop")
    except ListException as ex:
        print(ex.message)
    elem = input("Введите элемент списка: ")

print(list)