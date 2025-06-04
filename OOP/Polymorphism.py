class vehicle:
    def __init__(self, Model, Brand, Component):
        self.Model = Model  # instance var # public
        self.Brand = Brand
        self.Component = Component


class Plane(vehicle):
    pass


class Car(vehicle):
    pass


plane = Plane("Maria106", "Maria", "All")
car = Car("BMW", "BMW20054", "Main")

print(plane.Brand, plane.Model, plane.Component)
print(car.Brand, car.Model, car.Component)
