import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generate a random ID consisting of 15 lowercase letters.

    Returns:
        str: A random ID string.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Data class representing a student.

    Attributes:
        name (str): The first name of the student.
        surname (str): The last name (surname) of the student.
        active (bool, optional): Whether the student is
        active (default is True).
        login (str): The login name derived from the first
        name and surname (automatically generated).
        id (str): The student's ID (automatically generated).

    Example:
        student1 = Student(name="John", surname="Doe")
        print(student1.login)  # Output: "JohnDoe"
        print(student1.id)  # Output: (randomly generated ID)

        student2 = Student(name="Jane", surname="Smith", active=False)
        print(student2.login)  # Output: "JaneSmith"
        print(student2.id)  # Output: (randomly generated ID)
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """
        Automatically generate the login name after
        the initialization of the object.

        Returns:
            None.
        """
        self.login = (self.name[0] + self.surname).title()
