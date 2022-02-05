"""
создайте класс `Plane`, наследник `Vehicle`
"""

class Plane(Vehicle, cargo, max_cargo):
    def __init__(self):
        self.cargo = cargo
        self.max_cargo = max_cargo #в задании только мах в инициализаторе должен быть, как без него?

    def load_cargo(self, weight): #в задании "число", надо ли строго ставить, что это инт?
        if self.cargo + weight <= max_cargo:
            self.cargo += weight
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        current_cargo = self.cargo
        self.cargo = 0
        return current_cargo
