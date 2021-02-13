import random
from colorama import Fore
from colorama import Style

points= 0
all_points = 0
numbers = range(1,11)

print("Träna på multiplikationstabellen och vinn en överraskning")
print()
print()

def inputNumber(message):
    while True:
        try:
            userInput = int(input("Välj en tabell du vill träna på: "))
        except ValueError:
            print("Måste vara ett tal")
            continue
        else:
            return userInput
            break

def multiply(one, two):
    ans = one * two
    return ans

def game():
    points = 0
    tal = inputNumber("Vilken tabell vill du träna på: ")
    done = True
    while done:
        if points == 20:
            return
        rand = random.choice(numbers)
        answer = multiply(tal, rand)
        ditt_svar = int(input(f"{tal} * {rand} = "))

        print(f"{tal} * {rand} = {answer}")

        if ditt_svar == answer:
            points += 1
            print("YEY, snyggt!!")
            print(f"Poäng: {Fore.RED}{points}{Style.RESET_ALL}")
        else:
            print(f"Fel... Svaret är {answer}")
            print(f"Poäng: {Fore.BLUE}{points}{Style.RESET_ALL}")
        if points == 20:
            igen = str(input("Spela igen? Skriv ja eller nej: "))
            if igen == "ja":
                game()
            else:
                return
                   
game()


# lägg till tid
# lägg till totala poäng som adderas efter rundan om man vill fortsätta spela


