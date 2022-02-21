from homework_02.exceptions import LowFuelError, NotEnoughFuel
from abc import ABC


class Vehicle(ABC):
    def __init__(self, weight=100, fuel=500, fuel_consumption=20):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Fuel level is low")

    def move(self, distance):
        if self.fuel_consumption * distance <= self.fuel:
            self.fuel -= self.fuel_consumption * distance
        else:
            raise NotEnoughFuel("Not enough fuel")
