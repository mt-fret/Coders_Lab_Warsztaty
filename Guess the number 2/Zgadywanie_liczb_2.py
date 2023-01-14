def zgaduj():
    """User thinks of a number between 1 and 1000.
    by providing hints (too small/too big/right) computer tries to guess the number.

    :return: number guesses and total number of tries if number is correct.
    """
    print("Pomyśl liczbę od 0 do 1000, a ja ją zgadną w max. 10 próbach.")
    min = 0
    max = 1000
    correct = False
    guess_count = 0
    while not correct:
        guess = int((max-min)/2 + min)
        print(f"Zgaduję: {guess}")
        player_input = input("Is this your number?(too big/too small/right)")

        if player_input.lower() == "too big":
            max = guess
            guess_count += 1
            continue
        elif player_input.lower() == "too small":
            min = guess
            guess_count += 1
            continue
        elif player_input.lower() == "right":
            print(f"Wygrałem! W {guess_count} ruchach!")
            correct = True
        else:
            print("Nie oszukuj!")

zgaduj()