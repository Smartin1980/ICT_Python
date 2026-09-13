# 9. Python Quest – Final Game

## Ziel und Spielidee

Du kombinierst Variablen, Eingaben, Rechnungen, Verzweigungen, Schleifen und Zufall zu einem Text-Adventure. Du betrittst eine Höhle, kämpfst oder fliehst und erhältst bei einem Sieg Gold. Eigene Funktionen und Listen kannst du als Zusatzaufgabe ergänzen; im Grundspiel kommen sie noch nicht vor.

## Neue Werkzeuge

`random.randint(8, 15)` liefert eine zufällige ganze Zahl von 8 bis 15, beide Grenzen eingeschlossen.

`while monster_leben > 0 and leben > 0:` wiederholt den Kampf, solange **beide** Lebenswerte grösser als 0 sind. `and` bedeutet «und». Innerhalb der Schleife müssen sich Werte verändern oder ein `break` muss die Schleife beenden, damit sie nicht endlos läuft.

Menüeingaben bleiben Text. Vergleiche deshalb mit `"2"`, nicht mit der Zahl `2`.

## Erst überlegen

- Welche Werte brauchst du vor dem Kampf?
- Warum sollte ein besiegtes Monster nicht zurückschlagen?
- Wann brauchst du `break`?
- Du startest mit 10 Gold und gewinnst 20. Welcher Bestand soll erscheinen?

## Bauauftrag in Etappen

Erstelle die Datei und starte sie nach jeder Etappe.

1. **Start:** Importiere `random`, gestalte den Titel und frage `name` ab. Setze `leben` auf 100 und `gold` auf 10. Begrüsse die Person.
2. **Höhle:** Zeige die Auswahl `1 - Höhle betreten` und `2 - Weglaufen`. Frage `wahl` ab. Bei `"2"` endet die Geschichte mit einer Meldung. Sonst erscheint ein Monster mit 30 Leben.
3. **Kampf:** Wiederhole die Runden, solange beide Lebenswerte positiv sind. Zeige die Lebenswerte und die Auswahl `1 - Angreifen` und `2 - Fliehen`.
4. **Flucht:** Frage `aktion` ab. Bei `"2"` gib eine Fluchtmeldung aus und beende die Schleife.
5. **Angriff:** Ermittle 8 bis 15 zufällige Schadenspunkte, ziehe sie vom Monsterleben ab und zeige den Schaden.
6. **Sieg:** Prüfe sofort, ob das Monster höchstens 0 Leben hat. Gib eine Siegesmeldung aus, addiere 20 Gold, zeige den Bestand und beende die Schleife.
7. **Gegenangriff:** Lebt das Monster noch, verursacht es 5 bis 12 zufällige Schadenspunkte. Ziehe sie von `leben` ab und zeige den Schaden.
8. **Niederlage:** Prüfe nach der Schleife, ob `leben <= 0` gilt. Gib dann eine Niederlagenmeldung aus.

## Tipps

Die gesamte Kampflogik gehört in den `else`-Zweig der Höhlenwahl. Die Schleife liegt darin und benötigt eine weitere Einrückung. `break` verlässt die nächste umgebende Schleife. Prüfe den Sieg mit `<= 0`, weil Schaden die Monsterleben auch unter null bringen kann.

Im Grundspiel bedeutet `"2"` Weglaufen beziehungsweise Fliehen. Jede andere Eingabe führt in die Höhle beziehungsweise zum Angriff. Eine strengere Prüfung ist eine Zusatzaufgabe.

## Teste dich

| Weg | Eingaben | Erwartung |
| --- | --- | --- |
| Nach Hause | Name, dann `2` | Ende ohne Kampf |
| Flucht | Name, dann `1`, dann `2` | Flucht ohne Angriff oder Belohnung |
| Sieg | Name, dann immer `1` | Sieg und 30 Gold; kein Gegenangriff nach dem Sieg |
| Niederlage | Vorübergehend `leben = 1`, dann angreifen | Niederlage nach dem ersten Gegenangriff |

Stelle nach dem Niederlagentest die Startleben wieder auf 100. Mit den normalen Werten gewinnst du beim fortgesetzten Angreifen in höchstens vier Angriffen; die höchstens drei Gegenangriffe reichen nicht für eine Niederlage. Die Schadenszahlen können bei jedem Start anders sein.

## Zusatzaufgaben

Baue jeweils eine Erweiterung ein und teste sie:

- Frage bei ungültigen Menüeingaben erneut nach.
- Ermittle den Schaden in einer eigenen Funktion.
- Wähle einen Monsternamen zufällig aus einer Liste.
- Ergänze einen Heiltrank oder einen weiteren Raum.

Erkläre jemandem anhand deines Codes eine Kampfrunde: Woher kommt der Schaden, welcher Wert verändert sich und warum endet der Kampf?

## Vollständiger Lösungscode

Vergleiche erst nach deinem eigenen Versuch. Dieser Code enthält das vollständige Grundspiel; die freiwilligen Zusatzaufgaben sind nicht eingebaut.

Datei: `beispiele/mini-games/09_python_quest.py`

```python
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
```

[Zurück zur Übersicht](index.md)
