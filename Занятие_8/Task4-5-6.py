class SubCompanyException(Exception):
    def __init__(self, message):
        self.message = message


class WarehouseException(Exception):
    def __init__(self, message):
        self.message = message


class SubCompany:
    def __init__(self, name):
        self.name = name
        self.__technic_list = []

    def add_technic(self, technic):
        self.__technic_list.append(technic)

    def remove_technic(self, name):
        removable_technic = self.__get_removable_technic_by_name(name)
        if removable_technic is not None:
            self.__technic_list.remove(removable_technic)
        else:
            raise SubCompanyException("В подразделении компании нет удаляемой техники")

    def __get_removable_technic_by_name(self, removable_name):
        for technic in self.__technic_list:
            if technic.model == removable_name:
                return technic
        return None


class Warehouse:
    def __init__(self):
        self.printer_stock = { "count": 0, "list": [] }
        self.scanner_stock = { "count": 0, "list": [] }
        self.xerox_stock = { "count": 0, "list": [] }
        self.__sub_companies = [
            SubCompany("Бухгалтерия"),
            SubCompany("Руководство"),
            SubCompany("Вспомогательный персонал")
        ]

    def add_to_stock(self, technic):
        if type(technic) is Printer:
            self.printer_stock["count"] += 1
            self.printer_stock["list"].append(technic)
        elif type(technic) is Scanner:
            self.scanner_stock["count"] += 1
            self.scanner_stock["list"].append(technic)
        elif type(technic) is Xerox:
            self.xerox_stock["count"] += 1
            self.xerox_stock["list"].append(technic)
        else:
            raise WarehouseException("Введена неизвестная техника")

    def add_to_sub_company(self, subcompany_number, technic_number):
        if 0 < subcompany_number <= 3:
            if technic_number == 1 and self.printer_stock["count"] != 0:
                self.__sub_companies[subcompany_number - 1].add_technic(self.printer_stock["list"][0])
                self.printer_stock["list"] = self.printer_stock["list"][1:]
                self.printer_stock["count"] -= 1
            elif technic_number == 2 and self.scanner_stock["count"] != 0:
                self.__sub_companies[subcompany_number - 1].add_technic(self.scanner_stock["list"][0])
                self.scanner_stock["list"] = self.scanner_stock["list"][1:]
                self.scanner_stock["count"] -= 1
            elif technic_number == 3 and self.xerox_stock["count"] != 0:
                self.__sub_companies[subcompany_number - 1].add_technic(self.xerox_stock["list"][0])
                self.xerox_stock["list"] = self.xerox_stock["list"][1:]
                self.xerox_stock["count"] -= 1
            else:
                raise WarehouseException("Попытка добавления в подразделение техники, которой нет")
        else:
            raise WarehouseException("Попытка добавления в подразделение, которого нет")

    def remove_technic_from_sub_company(self, subcompany_number, technic_name):
        if 0 < subcompany_number <= 3:
            self.__sub_companies[subcompany_number - 1].remove_technic(technic_name)
        else:
            raise WarehouseException("Попытка добавления в подразделение, которого нет")


    @staticmethod
    def is_valid_number(number):
        return type(number) is int


class Technic:
    def __init__(self, model):
        self.model = model


class Printer(Technic):
    def __init__(self, cartridge_color_count):
        self.cartridge_color_count = cartridge_color_count


class Scanner(Technic):
    def __init__(self, definition):
        self.definition = definition


class Xerox(Technic):
    def __init__(self, speed):
        self.speed = speed


class Program:
    def __init__(self):
        self.__warehouse = Warehouse()

    def main(self):
        input_number = 0
        while input_number != 4:
            try:
                print("Выберите действие: ")
                print("1. Добавить технику на склад")
                print("2. Передать технику в подразделение")
                print("3. Списать технику с подразделения")
                print("4. Закончить программу")
                input_number = int(input())

                if input_number == 1:
                    self.add_technic_to_stock_menu()
                elif input_number == 2:
                    self.add_technic_to_sub_company_menu()
                elif input_number == 3:
                    self.remove_technic_from_sub_company_menu()

            except TypeError:
                print("Введено неверное значение")


    def add_technic_to_stock_menu(self):
        print("Выберите действие: ")
        print("1. Добавить принтер")
        print("2. Добавить сканер")
        print("3. Добавить ксерокс")
        input_number = int(input())

        if input_number == 1:
            try:
                model = input("Введите модель принтера: ")
                count = int(input("Введите число цветов принтера: "))
                printer = Printer(model, count)
                self.__warehouse.add_to_stock(printer)
                print("Принтер успешно добавлен на склад")
            except TypeError:
                print("Число цветов принтера должно быть целым числом")
        elif input_number == 2:
            try:
                model = input("Введите модель сканера: ")
                definition = float(input("Введите разрешение скана для данной модели: "))
                scanner = Scanner(model, definition)
                self.__warehouse.add_to_stock(scanner)
                print("Сканер успешно добавлен на склад")
            except TypeError:
                print("Разрешение скана должно быть вещественным числом")
        elif input_number == 3:
            try:
                model = input("Введите модель ксерокса: ")
                speed = int(input("Введите скорость ксерокса: "))
                xerox = Xerox(model, speed)
                self.__warehouse.add_to_stock(xerox)
                print("Ксерокс успешно добавлен на склад")
            except TypeError:
                print("Скорость ксерокса должна быть целым числом")


    def add_technic_to_sub_company_menu(self):
        try:
            print("Введите номер подразделения: ")
            print("1. Бухгалтерия")
            print("2. Руководство")
            print("3. Вспомогательный персонал")
            subcompany_number = int(input())

            print("Выберите тип техники со склада: ")
            print("1. Принтер")
            print("2. Сканер")
            print("3. Ксерокс")
            technic_number = int(input())

            self.__warehouse.add_to_sub_company(subcompany_number, technic_number)
            print("Техника успешно добавлена в подразделение")
        except TypeError:
            print("Введённые номера должны быть целым числом")
        except WarehouseException as wex:
            print(wex.message)
        except SubCompanyException as subex:
            print(subex.message)

    def remove_technic_from_sub_company_menu(self):
        try:
            print("Введите номер подразделения: ")
            print("1. Бухгалтерия")
            print("2. Руководство")
            print("3. Вспомогательный персонал")
            subcompany_number = int(input())

            technic_name = input("Введите имя техники: ")

            self.__warehouse.remove_technic_from_sub_company(subcompany_number, technic_name)
            print("Техника успешно списана с подразделения")
        except TypeError:
            print("Введённые номера должны быть целым числом")
        except WarehouseException as wex:
            print(wex.message)
        except SubCompanyException as subex:
            print(subex.message)


prog = Program()
prog.main()



