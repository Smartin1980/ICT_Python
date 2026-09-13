---
title: Python und Visual Studio Code installieren
description: Schritt-für-Schritt-Anleitung für den Python-Kurs
---

# Python und Visual Studio Code installieren

In dieser Anleitung richtest du deinen Computer für den Python-Kurs ein. Am Ende sind Python, VS Code und die Python-Erweiterung installiert. In der nächsten Anleitung lernst du die Oberfläche kennen und schreibst danach deine ersten Programme.

> **Zeitbedarf:** ungefähr 20–30 Minuten  
> **Du benötigst:** einen Computer mit Windows oder macOS und eine Internetverbindung

## Das installieren wir

Für den Kurs benötigen wir drei Bestandteile:

1. **Python** führt unsere Programme aus.
2. **Visual Studio Code**, kurz **VS Code**, ist unser Programmiereditor.
3. Die **Python-Erweiterung für VS Code** verbindet den Editor mit Python.

Für die neun [Mini-Games](mini-games/index.md) brauchst du keine zusätzlichen Python-Pakete. **Pygame Zero** kommt erst später beim grafischen Spiel **Achtung, Hai!** zum Einsatz.

---

## Teil 1: Python installieren

![Download Python](assets/images/Download_Python.avif)

### Windows

1. Öffne die offizielle Seite [python.org/downloads](https://www.python.org/downloads/).
2. Lade die aktuelle stabile Version von **Python 3** für Windows herunter.
3. Öffne die heruntergeladene Installationsdatei.
4. Starte die empfohlene Standardinstallation.
5. Warte, bis die Installation abgeschlossen ist.

> **Wichtig:** Falls der Installer die Option **Add Python to PATH** anzeigt, aktiviere sie. Dadurch kann Windows Python später im Terminal finden.

### macOS

1. Öffne [python.org/downloads](https://www.python.org/downloads/).
2. Lade die aktuelle stabile Version von **Python 3** für macOS herunter.
3. Öffne die heruntergeladene `.pkg`-Datei.
4. Folge dem Installationsassistenten und verwende die vorgeschlagenen Einstellungen.

### Installation kontrollieren

Öffne unter Windows **PowerShell** beziehungsweise unter macOS das **Terminal**.

Gib unter Windows ein:

```powershell
python --version
```

Falls dieser Befehl nicht funktioniert, versuche:

```powershell
py --version
```

Gib unter macOS ein:

```bash
python3 --version
```

Du solltest eine Ausgabe ähnlich wie diese erhalten:

```text
Python 3.x.x
```

Die genauen Zahlen dürfen anders aussehen. Entscheidend ist, dass die Version mit `3` beginnt.

---

## Teil 2: Visual Studio Code installieren

![Download VS Code](assets/images/Download_VS_Code.png)

1. Öffne [code.visualstudio.com](https://code.visualstudio.com/).
2. Lade die passende Version für dein Betriebssystem herunter.
3. Öffne die Installationsdatei.
4. Übernimm die vorgeschlagenen Einstellungen.
5. Starte **Visual Studio Code**.

Unter Windows sind folgende zusätzliche Optionen praktisch, falls sie angezeigt werden:

- **Add to PATH**
- **Open with Code** zum Kontextmenü hinzufügen
- VS Code als Editor für unterstützte Dateitypen registrieren

---

## Teil 3: Python-Erweiterung installieren

1. Öffne VS Code.
2. Klicke links auf das Symbol **Extensions** mit den vier Kästchen.
3. Alternativ kannst du die Tastenkombination `Ctrl` + `Shift` + `X` verwenden. Auf dem Mac ist es `Cmd` + `Shift` + `X`.
4. Suche nach `Python`.
5. Installiere die Erweiterung **Python** des Herausgebers **Microsoft**.

Die Erweiterung ergänzt unter anderem:

- farbige Darstellung von Python-Code,
- automatische Codevorschläge,
- Fehlermeldungen und Hinweise,
- Ausführen von Python-Dateien,
- Debugging zum schrittweisen Untersuchen eines Programms.

> Installiere nicht wahllos mehrere Python-Erweiterungen. Für den Kurs genügt zunächst die offizielle Erweiterung von Microsoft.

---

## Teil 4: Einen Kursordner anlegen

Speichere deine Programme nicht irgendwo zwischen Downloads und Dokumenten. Erstelle einen eigenen Kursordner.

1. Erstelle in deinen Dokumenten einen Ordner namens `python-kurs`.
2. Wähle in VS Code **File → Open Folder** beziehungsweise **Datei → Ordner öffnen**.
3. Öffne den Ordner `python-kurs`.
4. Bestätige bei einer Sicherheitsabfrage, dass du diesem selbst erstellten Ordner vertraust.

Im Explorer auf der linken Seite sollte nun der Ordner `python-kurs` erscheinen. Hier speicherst du deine eigenen Lösungen. Lege darin später den Unterordner `mini-games` für die neun Spiele an. Die Vorlagen im Kursprojekt liegen unter `beispiele/mini-games`; du findest ihren vollständigen Code auch auf den Lernseiten.

---

## Optional für später: Pygame Zero installieren

Pygame Zero benötigen wir erst für das grafische Spiel **Achtung, Hai!** im Projektordner `beispiele/Achtung_Hai`. Die Installation kann gemeinsam im Unterricht erfolgen. Für die Mini-Games kannst du diesen Abschnitt überspringen.

1. Öffne in VS Code über **Terminal → New Terminal** ein neues Terminal.
2. Gib unter Windows ein:

```powershell
python -m pip install pgzero
```

Wenn du Python über den Befehl `py` gestartet hast, verwende stattdessen:

```powershell
py -m pip install pgzero
```

Unter macOS verwendest du:

```bash
python3 -m pip install pgzero
```

3. Kontrolliere die Installation:

```powershell
python -m pip show pgzero
```

Unter macOS lautet der Befehl entsprechend:

```bash
python3 -m pip show pgzero
```

Falls du unter Windows `py` verwendest, prüfe mit `py -m pip show pgzero`. Die Ausgabe sollte unter anderem `Name: pgzero` und eine Versionsnummer enthalten. Verwende zum Installieren und Prüfen dieselbe Python-Installation wie in VS Code.

> Pygame Zero wird offiziell als Paket `pgzero` installiert. Dabei wird auch das benötigte Pygame mitinstalliert.

---

## Häufige Probleme

### `python` wurde nicht gefunden

- Schliesse VS Code vollständig und öffne es erneut.
- Probiere unter Windows `py --version`.
- Kontrolliere, ob Python wirklich installiert wurde.
- Installiere Python nochmals und aktiviere **Add Python to PATH**, falls diese Option angeboten wird.

### `pip` wurde nicht gefunden

Verwende nicht nur `pip`, sondern rufe es über Python auf:

```powershell
python -m pip install pgzero
```

Unter Windows kann auch Folgendes funktionieren:

```powershell
py -m pip install pgzero
```

---

## Abschlusskontrolle

Setze einen Haken, wenn der Schritt funktioniert. Die Häkchen werden nach dem Neuladen der Seite nicht gespeichert:

- [ ] Python 3 ist installiert.
- [ ] `python --version`, `py --version` oder `python3 --version` zeigt eine Version an.
- [ ] VS Code ist installiert.
- [ ] Die Erweiterung **Python von Microsoft** ist installiert.
- [ ] Der Ordner `python-kurs` ist in VS Code geöffnet.

Optional für später: Pygame Zero kannst du gemeinsam mit der Lehrperson vor **Achtung, Hai!** installieren.

Wenn alle Pflichtpunkte erfüllt sind, geht es weiter mit [VS Code Erste Schritte](vscode-erste-schritte.md). Dort lernst du zuerst Explorer, Editor und Terminal kennen und schreibst anschliessend deine ersten Programme.

---

## Hinweise für die Lehrperson

- Python und VS Code nach Möglichkeit vor dem ersten Kurstag installieren lassen.
- Für die Installationskontrolle fünf Minuten zu Beginn einplanen.
- Auf Schulgeräten vorab prüfen, ob Installationen und `pip` durch Richtlinien blockiert werden.
- Für alle Lernenden dieselbe Ordnerstruktur verwenden.
- Pygame Zero erst installieren, wenn es im Kurs benötigt wird.
- Bei Installationsproblemen zuerst den Versionsbefehl und die installierte Python-Erweiterung kontrollieren.
- Die ersten Programme folgen in «VS Code Erste Schritte», nachdem die Oberfläche erklärt wurde.

## Quellen und weiterführende Anleitungen

- [Offizielles Python-Downloadportal](https://www.python.org/downloads/)
- [Offizieller Python-Einstieg in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
- [Offizielle Python-Dokumentation für Windows](https://docs.python.org/3/using/windows.html)
- [Offizielle Python-Dokumentation für macOS](https://docs.python.org/3/using/mac.html)
- [Offizielle Installationsanleitung für Pygame Zero](https://pygame-zero.readthedocs.io/en/latest/installation.html)
- [DataCamp: Setting Up VS Code for Python](https://www.datacamp.com/tutorial/setting-up-vscode-python)
