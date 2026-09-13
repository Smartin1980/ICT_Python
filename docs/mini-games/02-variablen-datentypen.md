# 2. Character Creator – Variablen & Datentypen

## Ziel und Werkzeug

Du speicherst Eigenschaften einer Spielfigur. Mit `=` weist du einer Variable einen Wert zu.

| Typ | Bedeutung | Beispiel |
| --- | --- | --- |
| `str` | Text | `"Alex"` |
| `int` | Ganze Zahl | `100` |
| `float` | Kommazahl, in Python mit Punkt | `4.5` |
| `bool` | Wahr oder falsch | `True` oder `False` |

```python
punkte = 50
punkte = punkte - 10
print("Punkte:", punkte)
```

Python berechnet zuerst die rechte Seite und speichert das Ergebnis links. Kommas trennen bei `print()` Text und Werte.

## Erst überlegen

- Was unterscheidet `100` von `"100"`?
- Was gibt das Beispiel aus?
- Welcher Typ passt zur Eigenschaft «hat einen Schlüssel»?

## Bauauftrag

1. Speichere Alex, 100 Leben, Geschwindigkeit 4.5 und Schlüsselbesitz `False` in `name`, `leben`, `geschwindigkeit` und `hat_schluessel`.
2. Gib eine Überschrift und alle vier Eigenschaften mit Beschriftungen aus.
3. Ziehe 20 von `leben` ab und speichere das Ergebnis wieder in `leben`.
4. Gib eine Schadensmeldung und die verbleibenden Leben aus.

## Tipps

Text braucht Anführungszeichen, Zahlen und `False` nicht. Übertrage die Rechnung mit `punkte` auf die Lebenspunkte.

## Teste dich

Zuerst müssen 100 und nach dem Schaden 80 Leben erscheinen. Ändere die Startleben auf 60: Welches Ergebnis erwartest du? Prüfe auch die Ausgabe mit `hat_schluessel = True`.

## Zusatzaufgabe

Ergänze mindestens eine fünfte Eigenschaft, etwa Stärke oder Beruf, und gib sie aus.

## Vollständiger Lösungscode

Vergleiche erst nach deinem eigenen Versuch. Dieser Code enthält das vollständige Grundspiel; die freiwilligen Zusatzaufgaben sind nicht eingebaut.

Datei: `beispiele/mini-games/02_character_creator.py`

```python
name = "Alex"
leben = 100
geschwindigkeit = 4.5
hat_schluessel = False

print("=== CHARACTER CREATOR ===")
print("Name:", name)
print("Leben:", leben)
print("Geschwindigkeit:", geschwindigkeit)
print("Schlüssel:", hat_schluessel)

print()
leben = leben - 20
print("Autsch! Du verlierst 20 Leben.")
print("Leben:", leben)
```

[Weiter zum nächsten Spiel](03-operatoren.md)
