# Gross- und Kleinschreibung ist wichtig in Python.
# Python unterscheidet zwischen name, Name und NAME.
name = "Alex"
NamE = "Anna"

# Eine Bedingung mit Einrückung
if name >= "Alex":
    print(name)
else:
    print(NamE)

# Eine Funktion definiert wiederverwendbaren Code
def begruessung(spieler):
    return "Hallo " + spieler + "!"

print(begruessung(name))

woerter = ["python","computer","robo","game"]
print(woerter[0])

