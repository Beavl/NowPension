class NegativeLitres(Exception):
    pass

class Airplane:
    """
        Class representing an airplane.

    Attributes:
        consumption: an integer representing number of litres consumed per km of distance
        position (x, y): tuple of integer representing a position of the plane on a map.(1 km x 1 km grid)
        fuel level: a floating point number representing the current fuel level in litres
    """

    #constructor
    def __init__(self, init_x, init_y, consumption, initial_fuel_level):
        """
        Args:
            init_x (int): airplane initial position x
            init_y (int): airplane initial position x
            consumption (int): an integer representing number of litres consumed per km of distance
            initial_fuel_level (float): a floating point number representing the current fuel level in litres
        """
        self.position = (init_x,init_y)
        self.consumption = consumption
        self.fuel_level = initial_fuel_level

    def __calculate_distance(self, x1, y1, x2, y2):
        return ((x2 - x1) ** 2) + ((y2 - y1) ** 2)

    def refuel(self, litres):
        """
        Adds fuel to the airplane

        Args:
            litres (int): Number of litres to refuel

        Raises:
            NegativeLitres: litres is a negative number
        """

        if litres < 0:
            raise NegativeLitres('Litres can not be a negative number')
        self.fuel_level += litres

    def goto(self, x, y):
        """
        Moves the airplane to a new position if it has enough fuel.

        Args:
            x (int): x coordinate where the airplane has to move
            y (int): y coordinate where the airplane has to move

        Returns:
            result: If there is enough fuel returns True. Other case: False
        """
        result = False
        distance = self.__calculate_distance(self.position[0], self.position[1], x, y)

        # First check if there is enough fuel to move
        if self.consumption*distance < self.fuel_level:
            self.position = (x,y)
            self.fuel_level = self.fuel_level-(self.consumption*distance)
            result = True
        return result

