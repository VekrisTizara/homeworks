from abc import ABC


class Vehicle(ABC):
    def __init__(self, weight = 100, started = False, fuel = 500, fuel_consumption = 20):
        self.weight = weight
        self.fuel = fuel
        self.started = started  #можно ли не инициализировать?
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        if self.fuel_consumption * distance <= self.fuel:
            self.fuel -= self.fuel_consumption * distance
        else:
            raise NotEnoughFuel
