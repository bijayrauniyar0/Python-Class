class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
    def drive(self):
        return f"{self.brand}{self.model}is driving"
    
# class is made and the value is return by function created
#  electric car inhertis the car class, and adds ass per needs
#  super class is used in inheriting the upper class that is car
class ElectricCar(Car):
    def __init__(self,brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def charge(self):
        return f"{self.brand} {self.model} is charging"

# 
my_electric_car = ElectricCar("Telsa", "Mode 5", "100 kwh")

print("Brand:", my_electric_car.brand)
print("Model:", my_electric_car.model)

print("Battery Capcity:" ,my_electric_car.battery_capacity)
print(my_electric_car.drive())
print(my_electric_car.charge())






#multi inheritance
    
class Animal:
    def speak(self):
        return "Animal Speaks"

class Dog(Animal):
    def bark(self):
        return "Dog Barks"

class Labrador(Dog):
    def color(self):
        return "Labrador is brown"

my_labrador = Labrador()
print(my_labrador.speak())



#hiererchial

class Cat(Animal):
    def meow(self):
        return "Cat Meos"

my_dog = Dog()
my_cat = Cat()

print(my_dog.speak())