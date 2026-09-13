print("=== CODEKNACKER ===")

code = 482

for versuch in range(3):
    print()
    print("Versuch", versuch + 1, "von 3")
    tipp = int(input("Geheimcode: "))

    if tipp == code:
        print("Tresor geöffnet!")
        break
    else:
        print("Falscher Code.")

print("Spiel beendet.")
