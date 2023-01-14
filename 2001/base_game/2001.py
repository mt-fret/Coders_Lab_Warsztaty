import random
from kostka_do_gry import rzut
def gra():
    player_score = 0
    computer_score = 0
    tura = 1
    goal = 2001
    print("Welcome to 2001 game. The goal is to roll dice and add results until one player gets above 2001.")
    print("Press Enter to continue.")
    input()
    print(f"Round = {tura}")
    player_score += rzut("2D6")
    print(f"Player's score = {player_score}")
    computer_score += rzut("2D6")
    print(f"Computer's score = {computer_score}")
    tura += 1
    input()
    while True:
        player_roll = rzut("2D6")
        computer_roll = rzut("2D6")
        print(f"Round = {tura}")
        print(f"You rolled: {player_roll}")
        print(f"Computer rolled: {computer_roll}")
        if player_roll == 7:
            player_score = round(player_score/player_roll)
        elif player_roll == 11:
            player_score = player_score * player_roll
        else:
            player_score += player_roll
        if computer_roll == 7:
            computer_score = round(computer_score / computer_roll)
        elif computer_roll == 11:
            computer_score = computer_score * computer_roll
        else:
            computer_score += computer_roll
        print(f"Player's score = {player_score}")
        print(f"Computer's score = {computer_score}")
        if player_score >= goal:
            print("Player Won!")
            break
        if computer_score >= goal:
            print("Computer Won!")
            break
        tura += 1
        input()


if __name__ == '__main__':
    gra()
