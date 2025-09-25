class Engine:
    def engine_info(self):
        print("This is a diesel engine")
class wheels:
    def wheels_info(self):
        print("This car has 4 wheels")
class Truck(Engine, wheels):
    def truck_info(self):
        print("This is a truck")
mytruck = Truck()
mytruck.engine_info()   
mytruck.wheels_info()
mytruck.truck_info()