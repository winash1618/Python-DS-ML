"""
The goal of the exercise is to tackle the notion inheritance of class.
"""
class GotCharacter:
    """
    Create a GotCharacter class and initialize it with the following attributes:
        • first_name,
        • is_alive (by default is True).
    """

    def __init__(self, first_name, is_alive) -> None:
        """
        To be called automatically when GotCharacter class is instantiated.
        """
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    """
    Pick up a GoT House (e.g., Stark, Lannister...) and create a child class that inherits
    from GotCharacter and define the following attributes:
        • family_name (by default should be the same as the Class)
        • house_words (e.g., the House words for the Stark House is: "Winter is Coming")
    Add two methods to your child class:
        • print_house_words: prints the House words,
        • die: changes the value of is_alive to False.
    """

    def __init__(self, first_name=None, is_alive=True):
        """
        To be called automatically when Stark class is instantiated.
        """
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
        self.__dict__ = {'first_name': first_name, 'is_alive': is_alive, 
                         'family_name': self.family_name, 'house_words': self.house_words}

    def print_house_words(self) -> None:
        """
        prints the House words.
        """
        print(self.house_words)

    def die(self) -> None:
        """
        changes the value of is_alive to False
        """
        self.is_alive = False
