# 8. Monsterkampf – Funktionen

## Ziel und Werkzeug

Du definierst eine Funktion und verwendest ihren Rückgabewert.

```python
def verdoppeln(zahl):
    return zahl * 2

ergebnis = verdoppeln(4)
print(ergebnis)
```

`def` definiert eine Funktion. Der Parameter `zahl` erhält beim Aufruf hier den Wert 4. `return` gibt das Ergebnis zurück, das in `ergebnis` gespeichert wird. Die Ausgabe ist 8. Die Definition alleine führt den Funktionskörper noch nicht aus. `return` gibt auch keinen Text im Terminal aus; dafür brauchst du `print()`.

## Erst überlegen

- Was liefert `verdoppeln(7)` zurück?
- Ein Monster hat 30 Leben und erhält 10 Schaden. Was bleibt?
- Reicht ein Funktionsaufruf alleine, um einen gespeicherten Lebenswert zu verändern?

## Bauauftrag

1. Gib eine Überschrift aus. Setze `spieler_leben` auf 100 und `monster_leben` auf 30.
2. Definiere `angreifen(schaden)`. Gib darin zunächst einfach `schaden` zurück.
3. Zeige die Monsterleben an. `HP` steht für Lebenspunkte.
4. Rufe `angreifen(10)` auf und speichere das Ergebnis in `schaden`.
5. Ziehe `schaden` von `monster_leben` ab und speichere den neuen Wert.
6. Gib den Schaden und die restlichen Monsterleben aus.

## Tipps

Die Funktion gibt absichtlich nur den übergebenen Wert zurück. Das Abziehen passiert danach mit `monster_leben = monster_leben - schaden`. Die Spielerleben sind vorbereitet, werden aber noch nicht verwendet. Das Grundspiel zeigt einen Angriff, keinen Gegenangriff.

## Teste dich

Erwartet werden 30 HP, 10 Schaden und danach 20 HP. Ändere den Aufruf zu `angreifen(7)`: Nun müssen 23 HP bleiben. Die Funktionsdefinition muss vor dem Aufruf stehen.

## Zusatzaufgabe

Schreibe `heilen(leben)`, das `leben + 10` zurückgibt. Speichere das Ergebnis des Aufrufs in `spieler_leben` und gib es aus. Wie könntest du die Heilung auf höchstens 100 Leben begrenzen?

## 🤖 Frag deinen KI-Tutor

```text
Du bist mein Python-Tutor.
Erkläre mir anhand meines Codes den Unterschied zwischen einer Funktion definieren, einer Funktion aufrufen, einem Parameter übergeben und einem Wert mit `return` zurückgeben.
Nutze dabei mein Beispiel `angreifen(schaden)`.
Hilf mir herauszufinden, wann ich eine Funktion verwende und was der Aufruf genau macht.
Stelle mir danach zwei kurze Verständnisfragen.
Schreibe keine neue Monsterkampf-Lösung.

Mein Code:
[MEIN CODE]
```

## Vollständiger Lösungscode

Vergleiche erst nach deinem eigenen Versuch. Dieser Code enthält das vollständige Grundspiel; die freiwilligen Zusatzaufgaben sind nicht eingebaut.

Datei: `beispiele/mini-games/08_monsterkampf.py`

```python
print("=== MONSTERKAMPF ===")

spieler_leben = 100
monster_leben = 30

def angreifen(schaden):
    return schaden

print("Monster:", monster_leben, "HP")

schaden = angreifen(10)
monster_leben = monster_leben - schaden

print("Du verursachst", schaden, "Schaden.")
print("Monster:", monster_leben, "HP")
```

[Weiter zum nächsten Spiel](09-final-game.md)
