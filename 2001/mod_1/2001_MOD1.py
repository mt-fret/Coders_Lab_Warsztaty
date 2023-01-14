import random
from kostka_do_gry import rzut
kostki = ("D100", "D20", "D12", "D10", "D8", "D6", "D4", "D3")

def game_roll(roll, score):
    """

    :param roll: new roll made by user/computer
    :param score: old score
    :return: new score
    """
    if roll == 7:
        score = round(score / roll)
        return score
    elif roll == 11:
         score = score * roll
         return score
    else:
        score += roll
        return score

def gra():
    """Game of 2001.
    user and computer compete to acquire 2001 points from rolling dice.

    :return: winner, whoever is first to get to 2001 points
    """
    player_score = 0
    computer_score = 0
    tura = 1
    goal = 2001
    print("Welcome to 2001 game. The goal is to roll dice and add results until one player gets above 2001.")
    print("Press Enter to continue.")
    dice_type = input("What type of dice would you like to roll(D3,D4,D6,D8,D10,D12,D20,D100? ")
    print(f"Round = {tura}")
    player_score += rzut(f"2{dice_type}")
    print(f"Player's score = {player_score}")
    computer_dice = random.choice(kostki)
    computer_score += rzut(f"2{computer_dice}")
    print(f"Computer's score = {computer_score}")
    tura += 1
    while True:
        dice_type = input("What type of dice would you like to roll(D3,D4,D6,D8,D10,D12,D20,D100? ")
        player_roll = rzut(f"2{dice_type}")
        computer_dice = random.choice(kostki)
        computer_roll = rzut(f"2{computer_dice}")
        print(f"Round = {tura}")
        print(f"You rolled: {player_roll}")
        print(f"Computer choose: {computer_dice}")
        print(f"Computer rolled: {computer_roll}")
        player_score = game_roll(player_roll, player_score)
        computer_score = game_roll(computer_roll, computer_score)
        print(f"Player's score = {player_score}")
        print(f"Computer's score = {computer_score}")
        if player_score >= goal:
            print("Player Won!")
            break
        if computer_score >= goal:
            print("Computer Won!")
            break
        tura += 1



if __name__ == '__main__':
    gra()
