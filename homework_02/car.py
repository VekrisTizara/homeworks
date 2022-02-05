"""
создайте класс `Car`, наследник `Vehicle`
"""

class Car(Vehicle):
    def __init__(self, engine):
        self.engine = engine


    def set_engine(self, engine):
        self.engine = engine   #как сделать, чтобы именно экземпляр объекта Engine принимал?
