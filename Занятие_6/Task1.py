from time import sleep

class TrafficLight:
    def __init__(self, color="красный"):
        self.__color = color

    def running(self):
        while True:
            self.display()
            self.__color = "жёлтый"
            self.display()
            self.__color = "зелёный"
            self.display()
            self.__color = "жёлтый"
            self.display()
            self.__color = "красный"

    def display(self):
        if self.__color == "красный":
            print("\033[31m {}" .format("красный"))
            sleep(7)
        elif self.__color == "жёлтый":
            print("\033[33m {}" .format("жёлтый"))
            sleep(2)
        elif self.__color == "зелёный":
            print("\033[32m {}" .format("зелёный"))
            sleep(4)

traffic = TrafficLight()
traffic.running()
