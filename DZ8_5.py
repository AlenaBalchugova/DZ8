class Warehouse:
    def __init__(self, name):
        self.name = name
        self.inventory = {"Склад": {}, "Дирекция": {}, "Учет": {}, "Плановый": {}}

    def add(self, department, item, number):
        n = self.inventory[department].get(item, 0)
        self.inventory[department][item] = n + number

    def move(self, department, item, number):
        n = self.inventory["Склад"].get(item, 0)
        if n >= number:
            self.add("Склад", item, -number)
            self.add(department, item, number)
        else:
            print("Недостаточно оборудования на складе")

    def list_inventory(self, department):
        print(f'Список оргтехники {department}:')
        for k, v in self.inventory[department].items():
            print(f'{k.make} {k.model} - {v} шт.')

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

w.add("Склад", p1, 100)
w.add("Склад", p2, 120)
w.add("Склад", s1, 80)
w.add("Склад", x1, 30)

w.list_inventory("Склад")

w.move("Учет", p1, 10)
w.move("Учет", x1, 10)

w.list_inventory("Учет")
w.list_inventory("Склад")