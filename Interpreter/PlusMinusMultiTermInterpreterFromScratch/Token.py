#Baris Akkurt - GNU GPL v2

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        """String representation of the class instance.
        Example: Token('INTEGER', 5)
        """

        return "Token(" + self.type + ", " + self.value + ")"

    def __repr__(self):
        return self.__str__()