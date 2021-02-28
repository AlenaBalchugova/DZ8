class Warehouse:
    def __init__(self, name):
        self.name = name


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