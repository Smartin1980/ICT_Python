import random

print("=== WÖRTER RATEN ===")

woerter = ["python", "computer", "roboter", "gaming"]
geheimwort = random.choice(woerter)

tipp = input("Rate das geheime Wort: ")

if tipp.lower() == geheimwort:
    print("Richtig!")
else:
    print("Leider falsch.")
    print("Das Wort war:", geheimwort)
