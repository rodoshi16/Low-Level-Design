***Inheritance***

subclasses inherit all non private fields and methods of a the superclass. Subclass can override methods to provide diff implementation. 

Subclasses can also extend the superclass by adding new fields and methods

```
class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        self._make = make
        self._model = model
        self._year = year

    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")

    def display_info(self):
        print(f"{self._year} {self._make} {self._model}")

class ElectricCar(Vehicle):
    def __init__(self, make: str, model: str, year: int):
        super().__init__(make, model,year)
        self._battery_capacity = battery_capacity

class GasCar(Vehicle):
    def __init__(self, make: str, model: str, year: int, fuel_tank_size: float):
        super().__init__(make, model, year)
        self._fuel_tank_size = fuel_tank_size



```

Single inheritance - one child class extends a parent like Electric car extends Vehicle. 

Multi-level inheritance - When the child itself can also become a parent like Tesla extends from Electric Car. 

Hierarchial inheritance - when multiple child classes extend the same parent. 

Ex: electric, gas and hybrid all extend from vehicle

Multiple inheritance: when a child class extends more than one parent. Diamond problem: which parents method to use then? 

Python uses MRO - method resolution order: well defined algorithm that determines which parents method should take priority



**When to use inheritance?**

"is a" relationship - eletriccar is a vehicle, but a car has an engine - it is not an engine