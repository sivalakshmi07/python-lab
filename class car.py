class vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
class car(vehicle):
    def __init__(self, brand, color, model):
        super().__init__(brand, color)
        self.model = model
    def display_info(self):
        print("Brand:",{self.brand})
        print("Color:",{self.color})
        print("Model:",{self.model})
mycar = car("Toyota", "Red", "Corolla")
mycar.display_info()