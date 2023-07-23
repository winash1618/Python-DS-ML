from abc import ABC, abstractmethod

class Character(ABC):
    """Abstract class representing a character."""
    
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
        
    @abstractmethod
    def die(self):
        """Abstract method to set the character's is_alive attribute to False."""
        pass

class Stark(Character):
    """Class representing a Stark character."""
    
    def __init__(self, first_name, is_alive=True):
        """Doc string for constructor"""
        super().__init__(first_name, is_alive)
        
    
    def die(self):
        """Set the character's is_alive attribute to False."""
        self.is_alive = False
