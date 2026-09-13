# Zusatzübung: Begrüssung

Diese freiwillige Übung vertieft die Namensübung aus [VS Code Erste Schritte](../vscode-erste-schritte.md#ubung-dein-name). Versuche zuerst selbst eine Lösung zu schreiben.

## Erst überlegen

- Wie viele Eingaben brauchst du für einen Namen und ein Lieblingsspiel?
- Warum sollten die beiden Antworten unterschiedliche Variablennamen erhalten?

## Bauauftrag

Erstelle `begruessung.py` im Ordner `python-kurs`. Frage nach dem Namen und dem Lieblingsspiel. Gib danach beide Antworten aus, zum Beispiel:

```text
Wie heisst du? Ada
Was ist dein Lieblingsspiel? Minecraft
Hallo Ada
Dein Lieblingsspiel ist Minecraft
```

## Tipps

Verwende zweimal `input()` und speichere die Antworten in `name` und `lieblingsspiel`. Mit `print("Text", variable)` gibst du Text und einen gespeicherten Wert gemeinsam aus.

## Teste deine Lösung

Starte die Datei mit zwei unterschiedlichen Namen und Spielen. Probiere auch einen Spielnamen mit Leerzeichen. Werden die Antworten jeweils an der richtigen Stelle ausgegeben?

## Vollständiger Lösungscode

```python
name = input("Wie heisst du? ")
lieblingsspiel = input("Was ist dein Lieblingsspiel? ")
print("Hallo", name)
print("Dein Lieblingsspiel ist", lieblingsspiel)
```

[Weiter: Mini-Games](../mini-games/index.md)
