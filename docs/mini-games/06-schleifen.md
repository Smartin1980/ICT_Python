# 6. Codeknacker – Schleifen

## Ziel und Werkzeug

Die Spieler erhalten höchstens drei Versuche, einen Tresor zu öffnen. Eine `for`-Schleife wiederholt Befehle eine feste Anzahl Mal:

```python
for versuch in range(3):
    print("Versuch", versuch + 1)
```

`range(3)` liefert 0, 1 und 2. `break` beendet die Schleife vorzeitig.

Eine `while`-Schleife wiederholt Code, solange eine Bedingung wahr ist:

```python
geheimzahl = 7
tipp = 0
while tipp != geheimzahl:
    tipp = int(input("Dein Tipp: "))
```

Dieses Beispiel hat kein Versuchslimit. Der neue Tipp kann die Bedingung falsch machen. Für den Tresor verwendest du `for`.

## Erst überlegen

- Warum steht in der Ausgabe `versuch + 1`?
- Was würde nach einem Treffer passieren, wenn `break` fehlt?

## Bauauftrag

1. Gib eine Überschrift aus und speichere den Code 482 in `code`.
2. Wiederhole den Ratevorgang mit `for versuch in range(3):`.
3. Zeige die Versuchsnummer von 1 bis 3 und frage `tipp` als ganze Zahl ab.
4. Gib bei einem Treffer `Tresor geöffnet!` aus und beende die Schleife.
5. Gib sonst `Falscher Code.` aus.
6. Gib nach der Schleife einmal `Spiel beendet.` aus.

## Tipps

Abfrage und Entscheidung stehen eingerückt in der Schleife. Die Ausgabe bei einem Treffer und `break` stehen zusätzlich im `if`-Zweig, also insgesamt acht Leerzeichen eingerückt. Die letzte Ausgabe steht ausserhalb der Schleife ganz links.

## Teste dich

- Sofort `482`: keine weitere Frage nach dem Treffer.
- `111`, `222`, `482`: Treffer im dritten Versuch.
- Dreimal `111`: Ende nach drei Fehlmeldungen.

In allen Fällen erscheint `Spiel beendet.` genau einmal. Gib nur ganze Zahlen ein.

## Zusatzaufgabe

Erhöhe auf fünf Versuche und passe auch den Anzeigetext an. Kannst du die Gesamtzahl in einer Variable speichern und an beiden Stellen verwenden?

## Vollständiger Lösungscode

Vergleiche erst nach deinem eigenen Versuch. Dieser Code enthält das vollständige Grundspiel; die freiwilligen Zusatzaufgaben sind nicht eingebaut.

Datei: `beispiele/mini-games/06_codeknacker.py`

```python
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
```

[Weiter zum nächsten Spiel](07-listen.md)
