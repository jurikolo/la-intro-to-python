import math

print("Docs: https://docs.python.org/3.7/tutorial/classes.html#inheritance")

class Tire:
    """
    Tire represents a tire that would be used with an automobile.
    """

    def __init__(self, type, width, ratio, diameter, brand='', construction='R'):
        self.type = type
        self.width = width
        self.ratio = ratio
        self.diameter = diameter
        self.brand = brand
        self.construction = construction

    def __repr__(self):
        """
        Represent the tire information in the standard notation present
        on the side of the tire. Example: 'P205/55/R16'
        :return:
        """
        return(f"{self.type}{self.width}/{self.ratio}{self.construction}{self.diameter}")

    def circumference(self):
        """
        The circumference of the tire in inches.

        >>> tire = Tire('P', 205, 65, 15)
        >>> tire.circumference()
        80.1
        """
        total_diameter = self._side_wall_inches() * 2 + self.diameter
        return round(total_diameter * math.pi, 1)

    def _side_wall_inches(self):
        return (self.width * (self.ratio / 100)) / 25.4

class SnowTire(Tire):
    """
    Class inherited from Tire, adds chain_thickness parameter
    """
    def __init__(self, type, width, ratio, diameter, chain_thickness, brand='', construction='R'):
        # Tire.__init__(self, type, width, ratio, diameter, brand, construction)
        super().__init__(type, width, ratio, diameter, brand, construction)
        self.chain_thickness = chain_thickness

    def circumference(self):
        """
        The circumference of a tire w/ show chains in inches.

        >>> tire = SnowTire('P', 205, 65, 15, 2)
        >>> tire.circumference()
        92.7
        """
        total_diameter = (self._side_wall_inches() + self.chain_thickness) * 2 + self.diameter
        return round(total_diameter * math.pi, 1)

    def __repr__(self):
        return super().__repr__() + " (Snow)"

class Car:
    """
    Docstring describing the class
    """

    def __init__(self, color, tires):
        """
        Docstring describing the method
        """
        self.color = color
        self.tires = tires

    def description(self):
        """
        Describes the Car object
        :return:
        """
        print(f"Car has {self.color} color and {self.tires} tires")

    def wheel_circumference(self):
        if len(self.tires) > 0:
            return self.tires[0].circumference()
        else:
            return 0

tire = SnowTire('P', 205, 55, 16, 5)
tires = [tire, tire, tire, tire]
jk_car = Car("red", tires)
jk_car.description()
print(jk_car.wheel_circumference())
print()
print("To execute unit-test, run python3 -m doctest composition.py")

for tire in tires:
    print(f"{tire._side_wall_inches()}")