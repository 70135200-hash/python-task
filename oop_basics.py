class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(self.brand, "the car has started and its color is", self.color, "hai!")

my_car = Car("Toyota", "black")
my_car.start()