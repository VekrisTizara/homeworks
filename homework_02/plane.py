"""
создайте класс `Plane`, наследник `Vehicle`
"""
from exceptions import *
from base import Vehicle


class Plane(Vehicle):
    cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)  # как исходя из задания добавить в инит только макс?
        self.max_cargo = max_cargo

    def load_cargo(self, weight):  # в задании "число", надо ли строго ставить, что это инт?
        if self.cargo + weight <= self.max_cargo:
            self.cargo += weight
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        current_cargo = self.cargo
        self.cargo = 0
        return current_cargo
