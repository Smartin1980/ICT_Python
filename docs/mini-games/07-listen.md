# 7. Wörter raten – Listen

## Ziel und Werkzeug

Du speicherst Wörter in einer Liste und wählst zufällig eines aus.

```python
import random
woerter = ["python", "computer", "roboter"]
print(woerter[0])
geheimwort = random.choice(woerter)
```

Eckige Klammern begrenzen die Liste, Kommas trennen die Einträge. Der Index (die Position) beginnt bei 0, deshalb zeigt `woerter[0]` das Wort `python`. `import random` stellt Zufallswerkzeuge bereit; `random.choice()` wählt einen Listeneintrag.

`tipp.lower()` liefert den Tipp in Kleinbuchstaben: Aus `PYTHON` wird `python`.

## Erst überlegen

- Welches Wort steht im Beispiel an Index 2?
- Warum sollten alle Wörter der Liste kleingeschrieben sein?
- Muss der Zufall bei jedem Start ein anderes Wort auswählen?

## Bauauftrag

1. Importiere `random` und gib eine Überschrift aus.
2. Erstelle `woerter` mit `python`, `computer`, `roboter` und `gaming`.
3. Wähle einmal zufällig ein `geheimwort`.
4. Frage einen Tipp ab und vergleiche seine kleingeschriebene Form mit dem Geheimwort.
5. Gib bei einem Treffer `Richtig!` aus, sonst `Leider falsch.` und das gesuchte Wort.

## Tipps

Die Bedingung lautet `tipp.lower() == geheimwort`. Wähle das Wort vor der Eingabe. Zufall darf dasselbe Wort mehrmals hintereinander liefern. Es gibt einen Tipp pro Start.

## Teste dich

Gib `banane` ein: Dieser Tipp ist sicher falsch. Ersetze die Liste danach vorübergehend durch `["python"]`. Nun müssen `python` und `PYTHON` bei jeweils einem neuen Start richtig sein. Stelle anschliessend die Liste mit vier Wörtern wieder her.

## Zusatzaufgabe

Ergänze drei Wörter. Zeige vor der Eingabe die möglichen Wörter an, damit andere wissen, welche zur Auswahl stehen.

## 🤖 Frag deinen KI-Tutor

```text
Du bist mein Python-Tutor.
Erkläre mir anhand meines Codes, wie Listen funktionieren.
Warum beginnt der erste Index bei 0?
Was bedeutet `woerter[0]`?
Was macht `random.choice(woerter)`?
Warum wird `tipp.lower()` verwendet?
Stelle mir danach zwei kurze Verständnisfragen.
Schreibe keine neue Lösung.

Mein Code:
[MEIN CODE]
```

## Vollständiger Lösungscode

Vergleiche erst nach deinem eigenen Versuch. Dieser Code enthält das vollständige Grundspiel; die freiwilligen Zusatzaufgaben sind nicht eingebaut.

Datei: `beispiele/mini-games/07_woerterraten.py`

```python
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
```

[Weiter zum nächsten Spiel](08-funktionen.md)
