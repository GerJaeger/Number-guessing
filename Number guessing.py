import random

print("Dies ist ein Spiel mit Zahlen")
under = int(input("Bitte lege eine Untergrenze fest: "))
top = int(input("Bitte lege eine Obergrenze fest: "))

target = random.randint(under, top)
trys = (top - under)//2

while trys > 0:
    guess = int(input(f"Du hast {trys} Versuche. Errate deine Zahl: "))
    if guess == target:
        input(f"{target} ist die korrekte Zahl.")
        quit()
    elif guess > target:
        print("Deine Zahl ist zu groß")
        trys = trys - 1
    elif guess < target:
        print("Die Zahl ist zu klein")
        trys = trys - 1

input(f"Die Zahl war {target}.")
quit()