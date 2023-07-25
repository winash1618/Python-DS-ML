from S1E9 import Character
class Baratheon(Character):
    """Class representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Set the character's is_alive attribute to False."""
        self.is_alive = False

    def __str__(self):
        return f"Name: {self.first_name}, Family: {self.family_name}, Eyes: {self.eyes}, Hairs: {self.hairs}"

    def __repr__(self):
        return f" Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

class Lannister(Character):
    """Class representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Set the character's is_alive attribute to False."""
        self.is_alive = False

    def __str__(self):
        return f"Name: {self.first_name}, Family: {self.family_name}, Eyes: {self.eyes}, Hairs: {self.hairs}"

    def __repr__(self):
        return f" Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)