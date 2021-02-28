class InventoryError(Exception):
    def __init__(self, txt):
        self.txt = txt

class ParameterError(Exception):
    def __init__(self, txt):
        self.txt = txt

class Warehouse:
    def __init__(self, name):
        self.name = name
        self.inventory = {"Склад": {}, "Дирекция": {}, "Учет": {}, "Плановый": {}}

    def add(self, department, item, number):
        if isinstance(department, str) and isinstance(item, Equipment) and isinstance(number, int):
            n = self.inventory[department].get(item, 0)
            self.inventory[department][item] = n + number
        else:
            raise ParameterError("несовпадение типов аргументов")

    def move(self, department, item, number):
        if isinstance(department, str) and isinstance(item, Equipment) and isinstance(number, int):
            n = self.inventory["Склад"].get(item, 0)
            if n >= number:
                self.add("Склад", item, -number)
                self.add(department, item, number)
            else:
                raise InventoryError("недостаточно оборудования на складе")
        else:
            raise ParameterError("несовпадение типов аргументов")

    def list_inventory(self, department):
        print(f'Список оргтехники {department}:')
        for k, v in self.inventory[department].items():
            print(f'{k.make} {k.model} - {v} шт.')

        print("\n")


class Equipment:
    def __init__(self, id, make, model):
        self.id = id
        self.make = make
        self.model = model


class Printer(Equipment):
    def __init__(self, id, make, model, laser):
        super().__init__(id, make, model)
        self.laser = laser


class Scanner(Equipment):
    def __init__(self, id, make, model, dpi):
        super().__init__(id, make, model)
        self.dpi = dpi


class Xerox(Equipment):
    def __init__(self, id, make, model, speed):
        super().__init__(id, make, model)
        self.speed = speed


w = Warehouse("Склад оргтехники")
p1 = Printer(100001, "HP", "LaserJet 1000", True)
p2 = Printer(100002, "HP", "DeskJet 340", False)
s1 = Scanner(200001, "Samsung", "2020", 1200)
x1 = Xerox(300001, "Xerox", "Xerox", 10)

w.add("Склад", p1, 10)
w.add("Склад", p2, 12)
w.add("Склад", s1, 8)
w.add("Склад", x1, 3)

w.list_inventory("Склад")

try:
    w.move("Дирекция", p1, "1")
except ParameterError as err:
    print("Ошибка,", err)

try:
    w.move("Дирекция", p1, 1)
except InventoryError as err:
    print("Ошибка,", err)

try:
    w.move("Дирекция", x1, 1)
except InventoryError as err:
    print("Ошибка,", err)

try:
    w.move("Учет", p1, 9)
except InventoryError as err:
    print("Ошибка,", err)

try:
    w.move("Учет", x1, 3)
except InventoryError as err:
    print("Ошибка,", err)

w.list_inventory("Дирекция")
w.list_inventory("Учет")
w.list_inventory("Склад")