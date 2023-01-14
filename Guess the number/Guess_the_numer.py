import random

random_number = random.randint(1,100)

def guess_the_number():
    """User inputs a number until it is the same as randomly generated.

    :return: information if user guessed a number
    """

    correct = False
    while not correct:
        n = input("Guess the number: ")
        try:
            n = int(n)
        except ValueError:
            print("It's not a number")
            continue
        if n < random_number:
            print("Too small!")
            continue
        elif n > random_number:
            print("Too big!")
            continue
        else:
            print("You win!")
            correct = True


guess_the_number()