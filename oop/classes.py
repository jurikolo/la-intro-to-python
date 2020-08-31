print("Docs: https://docs.python.org/3/tutorial/classes.html#classes")
class Car:
    """
    Docstring describing the class
    """

    def __init__(self, color, transmission):
        """
        Docstring describing the method
        """
        self.color = color
        self.transmission = transmission

    def description(self):
        """
        Describes the Car object
        :return:
        """
        print(f"Car has {self.color} color and {self.transmission} speeds")

jk_car = Car("red", [1, 2, 3, 4, 5, 6])
jk_car.description()