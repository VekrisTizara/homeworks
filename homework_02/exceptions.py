"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(BaseException):
    pass

class NotEnoughFuel(BaseException):
    pass

class CargoOverLoad(BaseException):
    pass