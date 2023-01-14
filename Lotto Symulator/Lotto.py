import random

def lotto():
    skreślenia = []
    while len(skreślenia) < 6:
        try:
            num = int(input("Skreśl liczbę: "))
            if num not in range(1, 50):
                raise ValueError
            elif num in skreślenia:
                print("Ta liczba została już skreślona.")
                continue
            else:
                skreślenia.append(num)
        except ValueError:
            print("Tylko cyfry w przedziale 1-49")
    print(sorted(skreślenia))
    wyniki = []
    while len(wyniki) < 6:
        x = random.randint(1, 49)
        if x not in wyniki:
            wyniki.append(x)
    print(sorted(wyniki))
    score = 0
    for i in skreślenia:
        if i in wyniki:
            score += 0
    if score == 0:
        print("Nic nie trafione!")
    elif score <3:
        print(f"Przykro! Trafiłeś tylko {score}!")
    elif score >= 3:
        print(f"Wygrana! Trafiłeś aż {score}")


lotto()