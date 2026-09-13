# Dein erstes Python-Programm

In der [Installation](python-vscode-installation.md) und der [VS-Code-Einführung](vscode-erste-schritte.md) hast du zuerst `print("Hallo Python!")` ausgeführt. Jetzt untersuchst du die Begrüssung mit einer Eingabe genauer. Falls du sie dort bereits ausprobiert hast, kannst du direkt mit den Denkfragen beginnen.

## Erst überlegen

- Wo soll das Programm auf deinen Namen warten?
- Wie kann es sich die Eingabe merken?
- Was sollte sich ändern, wenn jemand anderes das Programm startet?

## Bauauftrag

1. Öffne deinen Ordner `python-kurs` in VS Code.
2. Öffne oder erstelle darin `hallo.py`.
3. Frage nach einem Namen und speichere die Antwort in `name`.
4. Gib `Hallo` und den eingegebenen Namen aus.

## Werkzeuge und Tipps

`input()` stellt eine Frage und wartet auf Enter. `name = ...` speichert die Antwort. `print()` gibt Text und Werte aus; mit einem Komma kannst du mehrere Teile trennen. Python setzt bei dieser Ausgabe ein Leerzeichen zwischen die Teile.

## Programm starten und prüfen

Speichere die Datei und verwende **Python-Datei ausführen** in VS Code. Alternativ öffnest du ein Terminal im Ordner `python-kurs`:

| Betriebssystem | Befehl |
| --- | --- |
| Windows | `python hallo.py`, alternativ `py hallo.py` |
| macOS / Linux | `python3 hallo.py` |

Klicke ins Terminal, tippe `Alex` und drücke Enter:

```text
Wie heisst du? Alex
Hallo Alex
```

Starte nochmals mit einem anderen Namen. Passt sich die Begrüssung an? Achte darauf, `print` kleinzuschreiben.

## Vollständiger Lösungscode

Dieser Code entspricht der Vorlage `beispiele/hallo.py` im Kursprojekt:

```python
name = input("Wie heisst du? ")
print("Hallo", name)
```

[Weiter: Mini-Games](mini-games/index.md)

Möchtest du Eingaben noch etwas üben? Löse die freiwillige [Zusatzübung Begrüssung](aufgaben/aufgabe-01.md).
