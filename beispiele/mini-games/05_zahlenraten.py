print("=== ZAHLENRATEN ===")

geheimzahl = 7
tipp = int(input("Rate meine Zahl von 1 bis 10: "))

if tipp == geheimzahl:
    print("Richtig!")
elif tipp < geheimzahl:
    print("Meine Zahl ist grösser.")
else:
    print("Meine Zahl ist kleiner.")
