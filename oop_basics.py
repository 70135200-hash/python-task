class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(self.brand, "the car has started and its color is", self.color, "hai!")

my_car = Car("Toyota", "black")
my_car.start()
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(self.brand, "the car has started and its color is", self.color, "hai!")

my_car = Car("Toyota", "black")
my_car.start()

class ElectricCar(Car):
    def __init__(self, brand, color, battery_capacity):
        super().__init__(brand, color)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(self.brand, "is charging with", self.battery_capacity, "kWh battery.")

my_ev = ElectricCar("Tesla", "white", 75)
my_ev.start()
my_ev.charge()
try:
    num1 = int(input("Pehla number likhein: "))
    num2 = int(input("Doosra number likhein: "))
    result = num1 / num2
    print("Jawab hai:", result)
except ZeroDivisionError:
    print("Ghalti: Kisi bhi number ko zero se divide nahi kiya ja sakta!")
except ValueError:
    print("Ghalti: Meherbani karke sirf numbers enter karein!")
    try:
 num = int(input("Enter a number: "))
  result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid number!")
else:
    print("Success! Result is:", result)
finally:
    print("Execution complete. This always runs.")
    