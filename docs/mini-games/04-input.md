# 4. Geheimcode – Eingaben

## Ziel und Werkzeug

Du fragst die Spieler nach ihren Angaben. `input()` wartet auf eine Eingabe und Enter und liefert immer Text. `int()` wandelt passenden Text in eine ganze Zahl um.

```python
name = input("Wie heisst du? ")
alter = int(input("Wie alt bist du? "))
```

Lies die zweite Zeile von innen nach aussen: fragen, umwandeln, speichern.

## Erst überlegen

- Warum braucht der Name kein `int()`?
- Was passiert wohl bei der Alterseingabe `zwölf`?
- Bleiben führende Nullen erhalten, wenn du `007` in eine Zahl umwandelst?

## Bauauftrag

1. Gib die Überschrift `=== GEHEIMCODE ===` aus.
2. Frage den Namen ab und speichere ihn in `name`.
3. Frage Alter und einen dreistelligen Code ab. Speichere sie mit `int()` in `alter` und `code`.
4. Gib nach einer Leerzeile eine Begrüssung, das Alter und den eingegebenen Code aus.

## Tipps

Du brauchst drei Eingaben. Bei `int(input(...))` musst du beide Klammern schliessen. Ein Leerzeichen am Ende der Frage trennt die Antwort vom Fragetext.

## Teste dich

- Gib `Alex`, `12` und `482` ein und kontrolliere die Ausgaben.
- Teste den Code `007`: Als ganze Zahl wird daraus `7`.
- Bei `zwölf` statt einer Zahl entsteht ein `ValueError`. Starte neu und gib Ziffern ein.

Das Grundspiel prüft weder die Dreistelligkeit noch ungültige Zahleneingaben.

## Zusatzaufgabe

Zeige das Alter in einem Jahr an. Überlege danach, wie du den Code speichern müsstest, damit führende Nullen erhalten bleiben.

## Vollständiger Lösungscode

Vergleiche erst nach deinem eigenen Versuch. Dieser Code enthält das vollständige Grundspiel; die freiwilligen Zusatzaufgaben sind nicht eingebaut.

Datei: `beispiele/mini-games/04_geheimcode.py`

```python
print("=== GEHEIMCODE ===")

name = input("Wie heisst du? ")
alter = int(input("Wie alt bist du? "))
code = int(input("Gib einen dreistelligen Geheimcode ein: "))

print()
print("Hallo", name)
print("Du bist", alter, "Jahre alt.")
print("Dein eingegebener Code lautet:", code)
```

[Weiter zum nächsten Spiel](05-verzweigungen.md)
