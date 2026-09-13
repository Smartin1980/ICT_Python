# 2. Umgebung einrichten

## Ziel

Du verwendest dein installiertes Python und VS Code weiter. Für die Grafik kommt **Pygame** dazu. Pygame und Pygame Zero sind unterschiedliche Werkzeuge; hier installieren wir `pygame`.

## 1. Projektordner öffnen

Erstelle `ki-snake` in deinem Ordner `python-kurs` und öffne **diesen Unterordner** in VS Code über «Datei → Ordner öffnen». Öffne «Terminal → Neues Terminal». Alle folgenden Befehle laufen im Ordner `ki-snake`.

```text
python-kurs/
└── ki-snake/
    ├── .venv/
    ├── 01_spielfenster.py
    ├── 02_bewegung.py
    ├── 03_snake.py
    └── lernprotokoll.md
```

Die Dateien erstellst du im Laufe der Etappen. `.venv` wird vom nächsten Befehl angelegt. Dieser Ordner enthält die Python-Umgebung mit den zusätzlichen Paketen für dieses Projekt; darin schreibst du keinen Spielcode.

## 2. Python-Umgebung und Pygame installieren

Führe die Befehle einzeln aus und warte jeweils auf das Ende. Nutze nur die Variante für dein Betriebssystem.

### Windows / PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install "pygame>=2.5,<3"
.\.venv\Scripts\python.exe -m pip show pygame
```

Wenn `py` fehlt, aber `python --version` funktioniert, verwende für den ersten Befehl `python -m venv .venv`.

### macOS / Linux

```bash
python3 -m venv .venv
./.venv/bin/python -m pip install "pygame>=2.5,<3"
./.venv/bin/python -m pip show pygame
```

Die letzte Ausgabe muss `Name: pygame` und eine Versionsnummer zeigen. Weil wir Python direkt aus `.venv` starten, brauchst du keine Aktivierung und keine Änderung der PowerShell-Ausführungsrichtlinie.

## 3. Interpreter auswählen

Öffne die Befehlspalette mit `Ctrl + Shift + P` (Mac: `Cmd + Shift + P`). Wähle `Python: Select Interpreter`, dann die Python-Version aus `.venv`. Falls sie nicht erscheint, wähle «Enter interpreter path» und die Datei `.venv/Scripts/python.exe` unter Windows beziehungsweise `.venv/bin/python` unter macOS/Linux.

## 4. KI-Chat vorbereiten

Öffne den von der Lehrperson freigegebenen KI-Chat im Browser, zum Beispiel euren vorhandenen ChatGPT-Zugang. Lege Browser und VS Code nebeneinander. Wir verwenden kurze Textaufträge und kopierten Code; Datei-Uploads, Bilderzeugung und eine Editor-Erweiterung sind für diese Aufgaben nicht nötig.

Teste einen Auftrag: «Erkläre mir in drei Sätzen den Unterschied zwischen einer Python-Liste und einer einzelnen Zahl.» Prüfe die Antwort mit deinem Vorwissen. Bei einer Zugangssperre oder einem Nutzungslimit verwendest du die Hinweise auf den Lernseiten oder die vorbereitete Antwort der Lehrperson.

## 5. Funktionstest

Kopiere den vollständigen Code von [Mein Spielfenster](03-spielfenster.md) in `01_spielfenster.py`. Speichere und starte über «Python-Datei ausführen» oder im Terminal:

| System | Befehl |
| --- | --- |
| Windows | `.\.venv\Scripts\python.exe 01_spielfenster.py` |
| macOS / Linux | `./.venv/bin/python 01_spielfenster.py` |

Ein dunkles Fenster mit grünem Quadrat soll erscheinen. Schliesse es über X beziehungsweise den Schliessen-Knopf. Starte erneut und teste Esc.

## Wenn etwas nicht funktioniert

| Problem | Nächster Schritt |
| --- | --- |
| `No module named pygame` | Prüfe den gewählten Interpreter; installiere mit dem Python aus derselben `.venv`. |
| `.venv` oder Spieldatei nicht gefunden | Kontrolliere, dass das Terminal im Ordner `ki-snake` steht und die Datei dort gespeichert ist. |
| Installation scheitert / keine passende Paketdatei | Hebe die genaue Fehlermeldung auf und hole die Lehrperson. Verwende die von ihr getestete Python-Version. |
| Linux meldet fehlendes `venv` | Die Lehrperson richtet die passende venv-Unterstützung über die Paketverwaltung ein. |
| Spiel reagiert nicht auf Tasten | Klicke zuerst in das Spielfenster. |

## Abschlusskontrolle

- [ ] Ich habe den Projektordner geöffnet und `.venv` erstellt.
- [ ] Pygame ist installiert und in VS Code ist der passende Interpreter gewählt.
- [ ] Das Testfenster öffnet und schliesst sich ohne Fehlermeldung.
- [ ] Mein KI-Zugang oder die vorbereitete Alternative ist verfügbar.

Häkchen werden nach dem Neuladen nicht gespeichert. Pygame-Quellen: [Dokumentation](https://www.pygame.org/docs/) und [Paketinformationen](https://pypi.org/project/pygame/).

[Weiter: Mein Spielfenster](03-spielfenster.md)
