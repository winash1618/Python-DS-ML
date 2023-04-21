"""
You have to make a program that will be an interactive guessing game. It will ask the
user to guess a number between 1 and 99. The program will tell the user if their input is
too high or too low. The game ends when the user finds out the secret number or types
exit. You will import the random module with the randint function to get a random
number. You have to count the number of trials and print that number when the user
wins.
"""
import random

def main() -> None:
    """
        Inorder to simplify the if __name__ == "__main__"
    """
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!\n")
    my_secret_random_number = random.randint(1, 99)
    print(my_secret_random_number)
    counter = 0
    while True:
        try:
            guess = input("What's your guess between 1 and 99?")
            if guess == "exit":
                print("Goodbye!")
                exit(0)
        except ValueError:
            print("That's not a number.")
            continue
        counter += 1
        if int(guess) > my_secret_random_number:
            print("Too high!")
        elif int(guess) < my_secret_random_number:
            print("Too low!")
        else:
            if my_secret_random_number == 42:
                print("The answer to the ultimate question of life, the universe and " +
                    "everything is 42.")
            else:
                print("Congratulations, you've got it!")
            if  my_secret_random_number == 42 && counter == 1:
                print("Congratulations! You got it on your first try!")
                exit(1)
            else:
                print(f"You won in {counter} attempts!")
                exit(1)

if __name__ == "__main__":
    main()