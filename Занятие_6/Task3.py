class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        print(self.name + ' ' + self.surname)

    def get_total_income(self):
        print(self._income['wage'] + self._income["bonus"])

position = Position("Иван", "Иванов", "Гений", 5000, 100)
position.get_full_name()
position.get_total_income()