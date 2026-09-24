# 3. Gold & Shop – Operatoren

## Ziel und Werkzeug

Du berechnest deinen Goldbestand nach einem Fund und einem Einkauf.

| Operator | Bedeutung             | Beispiel             |
| -------- | --------------------- | -------------------- |
| `+`      | Addition              | `8 + 3` ergibt `11`  |
| `-`      | Subtraktion           | `8 - 3` ergibt `5`   |
| `*`      | Multiplikation        | `8 * 3` ergibt `24`  |
| `/`      | Division              | `8 / 2` ergibt `4.0` |
| `//`     | Division mit Abrunden | `8 // 3` ergibt `2`  |
| `%`      | Divisionsrest         | `8 % 3` ergibt `2`   |
| `**`     | Potenz                | `2 ** 3` ergibt `8`  |

```python
gold = 20
gold = gold + 10
```

Die zweite Zeile speichert den neuen Goldbestand.

## Erst überlegen

- Du hast 20 Gold, findest 10 und bezahlst 15. Was bleibt?
- Verändert `print(gold - 15)` alleine den gespeicherten Goldbestand?
- Welcher Rest bleibt bei `17 % 2` und bei `18 % 2`?

## Bauauftrag

1. Starte mit `gold = 20`. Gib eine Überschrift und den Bestand aus.
2. Addiere den Fund von 10 Gold. Zeige Fund und neuen Bestand.
3. Speichere den Schwertpreis 15 in `schwert_preis` und ziehe ihn vom Gold ab.
4. Gib den Kaufpreis und das restliche Gold aus.
5. Prüfe zum Schluss, ob `zahl = 17` gerade oder ungerade ist, und gib das Ergebnis aus.

## Tipps

Du kannst mit Variablen rechnen: `gold - schwert_preis`. Speichere das Ergebnis wieder in `gold`.

Für die letzte Teilaufgabe brauchst du einen Vorgriff auf [Kapitel 5](05-verzweigungen.md): `if` bedeutet «wenn», `else` bedeutet «sonst». `==` vergleicht Werte. Gilt `zahl % 2 == 0`, ist die Zahl gerade. Nach `if` mit seiner Bedingung und nach `else` steht ein Doppelpunkt. Die zugehörige Ausgabe folgt in der nächsten Zeile, um vier Leerzeichen eingerückt.

## Teste dich

Die Goldstände müssen 20, 30 und 15 sein. Prüfe die Zahlen 17 und 18: Erwartet werden `UNGERADE!` und `GERADE!`. Was passiert bei einem Preis von 40? Der einfache Shop zieht den Preis auch bei zu wenig Gold ab.

## Zusatzaufgabe

Kaufe zusätzlich zwei Heiltränke zu je 3 Gold. Berechne ihren Gesamtpreis mit `*`. Mit Kapitel 5 kannst du später Käufe bei zu wenig Gold verhindern.

## 🤖 Frag deinen KI-Tutor

```text
Du bist mein Python-Tutor.
Erkläre mir anhand meines Codes, wie die Operatoren funktionieren.
Zeige mir, wie ich die Werte in meinen Variablen verändere und warum die Berechnungen so funktionieren.
Erkläre mir besonders, warum `print(gold - 15)` den gespeicherten Wert von `gold` nicht verändert.
Gib mir einen kleinen Hinweis, wenn ich selbst noch überlegen möchte.
Stelle mir danach zwei Verständnisfragen.

Mein Code:
[MEIN CODE]
```

## Vollständiger Lösungscode

Vergleiche erst nach deinem eigenen Versuch. Dieser Code enthält das vollständige Grundspiel; die freiwilligen Zusatzaufgaben sind nicht eingebaut.

Datei: `beispiele/mini-games/03_gold_shop.py`

```python
gold = 20

print("=== GOLD & SHOP ===")
print("Du startest mit", gold, "Gold.")

gold = gold + 10
print("Du findest 10 Gold.")
print("Gold:", gold)

schwert_preis = 15
gold = gold - schwert_preis
print("Du kaufst ein Schwert für", schwert_preis, "Gold.")
print("Restliches Gold:", gold)

zahl = 17
print()
print("Bonus-Challenge:")
print("Ist", zahl, "gerade oder ungerade?")

if zahl % 2 == 0:
    print("GERADE!")
else:
    print("UNGERADE!")
```

[Weiter zum nächsten Spiel](04-input.md)
