class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police
        print(speed, self.color, self.name, self.is_police)

    def go(self, speed):
        print("Машина поехала")
        self.speed = speed

    def stop(self):
        print("Машина остановилась")
        self.speed = 0

    def turn(self, direction):
        print("Машина повернула ", direction)

    def show_speed(self):
        print("Скорость машины: ", self.speed)

class TownCar(Car):
    def show_speed(self):
        print("Скорость машины: ", self.speed)
        if self.speed > 60:
            print("Скорость превышена")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print("Скорость машины: ", self.speed)
        if self.speed > 40:
            print("Скорость превышена")

class PoliceCar(Car):
    pass

definition_car_1 = TownCar(80, "red", "Lamborghini", False)
definition_car_1.go(80)
definition_car_1.show_speed()
definition_car_1.turn("направо")
definition_car_1.stop()
print()

definition_car_2 = SportCar(60, "yellow", "Ford", False)
definition_car_2.go(60)
definition_car_2.show_speed()
definition_car_2.turn("налево")
definition_car_2.stop()
print()

definition_car_3 = WorkCar(50, "blue", "Audi", False)
definition_car_3.go(50)
definition_car_3.show_speed()
definition_car_3.turn("назад")
definition_car_3.stop()
print()

definition_car_4 = PoliceCar(30, "pink", "Toyota", True)
definition_car_4.go(30)
definition_car_4.show_speed()
definition_car_4.turn("неизвестно куда")
definition_car_4.stop()
