"""
создайте класс `Car`, наследник `Vehicle`
"""

from base import Vehicle

class Car(Vehicle):
    engine = None

    def __init__(self, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)


    def set_engine(self, engine):
        self.engine = engine   #как сделать, чтобы именно экземпляр объекта Engine принимал?
