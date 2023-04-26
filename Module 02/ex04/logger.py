"""
In this exercise, you will learn about decorators and we are not talking about the
decoration of your room. The @log will write info about the decorated function in a
machine.log file.
"""
import time
from random import randint
import os

def log(func):
    """
    You have to create the log decorator in the same file.
    Pay attention to all the different actions logged at the
    call of each methods. You may notice the username from 
    environment variable is written to the log file.
    """
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        stdout = os.dup(1)
        with open("machine.log", "a", encoding="utf-8") as file:
            os.dup2(file.fileno(), 1)
            print("(cmaxtime)Running: ", end='')
            if func.__name__ == 'start_machine':
                print(f"{'Start Machine':20}", end='')
            elif func.__name__ == 'boil_water':
                print(f"{'Boil Water':20}", end='')
            elif func.__name__ == 'make_coffee':
                print(f"{'Make Coffee':20}", end='')
            elif func.__name__ == 'add_water':
                print(f"{'Add Water':20}", end='')
            print(f"[ exec-time = {round(time.time() - start_time, 5)} ms ]")
        os.dup2(stdout, 1)
        return result
    return wrapper

class CoffeeMachine():
    """
    Class of coffee machine
    """
    water_level = 100
    @log
    def start_machine(self):
        """
        handle machine start
        """
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
    @log
    def boil_water(self):
        """
        handles boiling water
        """
        return "boiling..."
    @log
    def make_coffee(self):
        """
        handles making coffee
        """
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    @log
    def add_water(self, water_level):
        """
        handles adding water
        """
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")
