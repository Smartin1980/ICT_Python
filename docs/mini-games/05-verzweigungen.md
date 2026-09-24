# 5. Zahlenraten – Verzweigungen

## Ziel und Werkzeug

Dein Ratespiel reagiert auf einen Tipp. `if` prüft eine Bedingung. Ist sie falsch, prüft Python `elif` («sonst wenn»). Trifft keine zu, läuft `else`. Nur einer dieser Zweige wird ausgeführt.

| Vergleich | Bedeutung           |
| --------- | ------------------- |
| `==`      | gleich              |
| `!=`      | ungleich            |
| `<`       | kleiner             |
| `>`       | grösser             |
| `<=`      | kleiner oder gleich |
| `>=`      | grösser oder gleich |

Achtung: `=` speichert einen Wert, `==` vergleicht zwei Werte. Nach einer Bedingung steht ein Doppelpunkt. Der zugehörige Code wird mit vier Leerzeichen eingerückt.

## Erst überlegen

- Die Geheimzahl ist 7 und dein Tipp ist 3. Ist die gesuchte Zahl grösser oder kleiner?
- Welche drei Fälle muss das Spiel unterscheiden?

## Bauauftrag

1. Gib eine Überschrift aus und speichere 7 in `geheimzahl`.
2. Frage einen Tipp von 1 bis 10 ab und wandle ihn mit `int()` um.
3. Gib bei einem Treffer `Richtig!` aus.
4. Ist der Tipp kleiner als die Geheimzahl, gib `Meine Zahl ist grösser.` aus.
5. Gib sonst `Meine Zahl ist kleiner.` aus.

## Tipps

Beginne mit `if tipp == geheimzahl:`. Der zweite Zweig braucht `elif` und `<`. Hinter `else` steht keine Bedingung. Alle drei Schlüsselwörter stehen gleich weit links.

## Teste dich

Starte für jeden Test neu; das Grundspiel bietet einen Versuch pro Start.

| Tipp | Erwartete Ausgabe         |
| ---- | ------------------------- |
| `7`  | `Richtig!`                |
| `3`  | `Meine Zahl ist grösser.` |
| `9`  | `Meine Zahl ist kleiner.` |

Verwende ganze Zahlen. Der Bereich 1 bis 10 wird noch nicht geprüft; Texteingaben werden nicht abgefangen.

## Zusatzaufgabe

Ändere die Geheimzahl und teste alle drei Fälle erneut. Ergänze eine eigene Meldung für Zahlen ausserhalb von 1 bis 10.

## 🤖 Frag deinen KI-Tutor

```text
Du bist mein Python-Tutor.
Erkläre mir anhand meines Codes, wie `if`, `elif` und `else` den Programmfluss steuern.
Lass uns gemeinsam verschiedene Werte durch das Programm gehen.
Beispiel: Geheimzahl = 7.
Was passiert bei:
- Tipp 3
- Tipp 7
- Tipp 9
Stelle mir danach zwei kurze Verständnisfragen.
Schreibe keine neue Lösung.

Mein Code:
[MEIN CODE]
```

## Vollständiger Lösungscode

Vergleiche erst nach deinem eigenen Versuch. Dieser Code enthält das vollständige Grundspiel; die freiwilligen Zusatzaufgaben sind nicht eingebaut.

Datei: `beispiele/mini-games/05_zahlenraten.py`

```python
print("=== ZAHLENRATEN ===")

geheimzahl = 7
tipp = int(input("Rate meine Zahl von 1 bis 10: "))

if tipp == geheimzahl:
    print("Richtig!")
elif tipp < geheimzahl:
    print("Meine Zahl ist grösser.")
else:
    print("Meine Zahl ist kleiner.")
```

[Weiter zum nächsten Spiel](06-schleifen.md)
