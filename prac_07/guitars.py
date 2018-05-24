""" Do From Scratch Exercise"""



YEAR = 2017


class Guitar:
    """
    """
    def __init__(self):
        """
        Initialise a Guitar instance.
        name: string, year: int, year: float
        """
        self.name = ""
        self.year = 0
        self.cost = 0

    def __str__(self):
        """
        Return a string representation of a guitar.
        """
        return '{} ({}) : ${:.2f}'.format(self.name, self.year, self.cost)

    def add_name(self, name):
        """
        Adds a name to the guitar object
        """
        self.name = name

    def add_year(self, year):
        """
        Adds a year to the guitar object
        """
        self.year = year

    def add_cost(self, cost):
        """
        Adds a cost to the guitar object
        """
        self.cost = cost

    def get_age(self):
        """
        Return a integer representing the age of the object.
        """
        age = YEAR - self.year
        return age

    def is_vintage(self, age):
        """
        Returns a True statement if the object if older that 50 years.
        """
        if 50 <= age:
            return True
        else:
return False