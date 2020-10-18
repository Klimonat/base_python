class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    def draw(self):
        print("Рисуем ручкой")

class Pencil(Stationery):
    def draw(self):
        print("Делаем набросок карандашом")

class Handle(Stationery):
    def draw(self):
        print("Делаем обводку маркером")

stat = Stationery("Название")
stat.draw()
print()

pen = Pen("Название")
pen.draw()
print()

pencil = Pencil("Название")
pencil.draw()
print()

handle = Handle("Название")
handle.draw()
print()

