# Einfaches Snake für den Unterricht

Die drei Dateien sind eigenständig startbare Etappen. Es werden keine Bilder, Sounds oder API-Schlüssel benötigt. Snake Advanced bleibt ein separates Kreativprojekt.

| Datei | Inhalt |
| --- | --- |
| `01_spielfenster.py` | Fenster, Rasterposition und grünes Quadrat |
| `02_bewegung.py` | Automatische Bewegung, Pfeiltasten, Halt am Rand |
| `03_snake.py` | Körper, Futter, Punkte, Wand- und Selbstkollision, Neustart |
| `lernprotokoll.md` | Vorlage zum Dokumentieren von KI-Hilfe und Tests |

Öffne diesen Spielordner in VS Code. Unter Windows im Terminal:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe 03_snake.py
```

Unter macOS / Linux:

```bash
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python 03_snake.py
```

Wähle in VS Code über `Python: Select Interpreter` ebenfalls Python aus `.venv`. Eine Aktivierung der Umgebung ist für die gezeigten Befehle nicht erforderlich.

Pfeiltasten steuern. Esc oder das Fensterschliessen beendet alle Etappen. Im vollständigen Spiel startet R nach einem Spielende neu. Es gibt keine direkte Kehrtwende und höchstens eine Drehung pro Bewegungsschritt. Etappe 2 hält am Rand an; Etappe 3 beendet dort das Spiel. Punkte stehen im Fenstertitel. Ist das Raster voll, ist das Spiel gewonnen.

Die Lernseiten und der 120-Minuten-Plan liegen unter `docs/ki-snake` im Projekt. Die ersten zwei Stunden führen bis zur ersten geprüften KI-Änderung; die vollständige Snake-Etappe ist für die Fortsetzung vorgesehen.
