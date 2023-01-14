import random

kostki = ("D100", "D20", "D12", "D10", "D8", "D6", "D4", "D3")
def roll(y):
    """Function takes a size of a dice and performs a roll.

    :param y: size of dice
    :return: result of a dice roll
    """
    return random.randint(1, y)

def rzut(kod):
    for kostka in kostki:
        if kostka in kod:
            try:
                ilosc, dodatek = kod.split(kostka)
            except ValueError:
                return 'Zły kod'
            y = int(kostka[1:])
            break
    else:
        return 'Nie ma takiej kostki'
    try:
        ilosc = int(ilosc) if ilosc else 1
    except ValueError:
        return 'Zły kod'
    try:
        dodatek = int(dodatek) if dodatek else 0
    except ValueError:
        return 'Zły kod'
    wynik = 0
    for i in range(ilosc):
        wynik += roll(y)
    wynik += dodatek
    return wynik

print(rzut("2D100+7"))
