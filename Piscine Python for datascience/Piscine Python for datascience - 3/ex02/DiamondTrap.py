from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Class representing the King, inheriting from Baratheon and Lannister.

    Attributes:
        first_name (str): The first name of the King.
        is_alive (bool): Whether the King is alive or not. Default is True.

    Methods:
        __init__(first_name, is_alive=True):
            Initializes a new King instance.

        set_eyes(color):
            Sets the eye color of the King.

        set_hairs(color):
            Sets the hair color of the King.

        get_eyes():
            Returns the current eye color of the King.

        get_hairs():
            Returns the current hair color of the King.
    """

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """
        Set the eye color of the King.

        Args:
            color (str): The new eye color to set for the King.
        """
        self.eyes = color

    def set_hairs(self, color):
        """
        Set the hair color of the King.

        Args:
            color (str): The new hair color to set for the King.
        """
        self.hairs = color

    def get_eyes(self):
        """
        Get the current eye color of the King.

        Returns:
            str: The current eye color of the King.
        """
        return self.eyes

    def get_hairs(self):
        """
        Get the current hair color of the King.

        Returns:
            str: The current hair color of the King.
        """
        return self.hairs
