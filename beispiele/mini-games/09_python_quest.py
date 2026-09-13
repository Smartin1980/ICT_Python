import random

print("========================")
print("      PYTHON QUEST")
print("========================")
print()

name = input("Wie heisst du? ")
leben = 100
gold = 10

print()
print("Hallo", name + "!")
print("Du stehst vor einer dunklen Höhle.")
print("1 - Höhle betreten")
print("2 - Weglaufen")

wahl = input("> ")

if wahl == "2":
    print("Du gehst nach Hause. Ende.")
else:
    monster_leben = 30
    print()
    print("Ein Monster erscheint!")

    while monster_leben > 0 and leben > 0:
        print()
        print("Dein Leben:", leben)
        print("Monster:", monster_leben)
        print("1 - Angreifen")
        print("2 - Fliehen")

        aktion = input("> ")

        if aktion == "2":
            print("Du fliehst aus der Höhle.")
            break

        schaden = random.randint(8, 15)
        monster_leben = monster_leben - schaden
        print("Du verursachst", schaden, "Schaden.")

        if monster_leben <= 0:
            print("Du hast das Monster besiegt!")
            gold = gold + 20
            print("Du findest 20 Gold.")
            print("Gold:", gold)
            break

        monster_schaden = random.randint(5, 12)
        leben = leben - monster_schaden
        print("Das Monster verursacht", monster_schaden, "Schaden.")

    if leben <= 0:
        print("Du wurdest besiegt.")
