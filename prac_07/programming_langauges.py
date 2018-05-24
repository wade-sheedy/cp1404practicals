


class ProgrammingLanguage:
    """
    Represent a programing language object.
    """

    def __init__(self, name, typing, reflection, year):
        """
        Initialise a Programing Language instance.
        name: string, typing: string, reflection: string, year: int
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """
        Return a string representation of a Programing Language.
        """
        return '{}, {}, Reflection={}, First appeared in {}'.format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        """
        Return a boolean
        """
        return self.reflection == 'Yes'