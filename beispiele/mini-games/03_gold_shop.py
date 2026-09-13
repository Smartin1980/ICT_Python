gold = 20

print("=== GOLD & SHOP ===")
print("Du startest mit", gold, "Gold.")

gold = gold + 10
print("Du findest 10 Gold.")
print("Gold:", gold)

schwert_preis = 15
gold = gold - schwert_preis
print("Du kaufst ein Schwert für", schwert_preis, "Gold.")
print("Restliches Gold:", gold)

zahl = 17
print()
print("Bonus-Challenge:")
print("Ist", zahl, "gerade oder ungerade?")

if zahl % 2 == 0:
    print("GERADE!")
else:
    print("UNGERADE!")
