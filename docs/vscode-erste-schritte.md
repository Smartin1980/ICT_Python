---
title: VS Code bedienen
description: Erste Schritte mit VS Code für den Python-Kurs
---

# Erste Schritte mit VS Code

VS Code ist unser **digitaler Arbeitsplatz zum Programmieren**. Ähnlich wie Word beim Schreiben von Texten hilft, unterstützt uns VS Code beim Schreiben von Programmen.

Für unseren Kurs brauchst du in VS Code zunächst nur wenige Funktionen. Voraussetzung ist die abgeschlossene [Installation von Python und VS Code](python-vscode-installation.md). Hier lernst du zuerst die Oberfläche kennen. Anschliessend schreibst und startest du deine ersten beiden Programme.

## Lernziele

Nach dieser Anleitung kannst du:

- einen Kursordner in VS Code öffnen,
- eine Python-Datei erstellen,
- Python-Code schreiben und speichern,
- ein Python-Programm starten,
- Ausgaben und einfache Fehlermeldungen lesen.

---

## Die vier wichtigsten Bereiche

| Bereich                    | Erklärung                                             |
| -------------------------- | ----------------------------------------------------- |
| **Explorer**               | Hier siehst du deine Ordner und Dateien.              |
| **Editor**                 | Hier schreibst und bearbeitest du deinen Python-Code. |
| **Start-Schaltfläche `▶`** | Damit führst du dein Programm aus.                    |
| **Terminal**               | Hier erscheinen Ausgaben und Fehlermeldungen.         |

> **Wichtig:** VS Code kann sehr viel. Die übrigen Symbole und Funktionen darfst du am Anfang ignorieren.

---

## 1. Kursordner erstellen

Verwende den Ordner aus der Installation. Falls er noch fehlt, erstelle unter **Dokumente** einen neuen Ordner:

```text
python-kurs
```

Später kann dieser Ordner beispielsweise so aufgebaut sein:

```text
python-kurs
├── hallo.py
├── begruessung.py
└── mini-games
    ├── 01_game_intro.py
    ├── 02_character_creator.py
    └── ...
```

Die Dateien entstehen im Laufe der Übungen; `begruessung.py` gehört zur freiwilligen Zusatzübung. Speichere deine eigenen Spiele unter `python-kurs/mini-games`. Die fertigen Vorlagen liegen im Kursprojekt unter `beispiele/mini-games` und stehen auch vollständig auf den Lernseiten.

## 2. Kursordner in VS Code öffnen

1. Starte VS Code.
2. Wähle **Datei → Ordner öffnen**.
3. Wähle den Ordner `python-kurs` aus.
4. Klicke auf **Ordner auswählen**.

> **Merksatz:** Öffne in VS Code immer den ganzen Kursordner und nicht nur eine einzelne Datei.

## 3. Eine Python-Datei erstellen

1. Klicke links im Explorer auf **Neue Datei**.
2. Gib als Dateinamen ein:

```text
hallo.py
```

Die Dateiendung `.py` zeigt dem Computer und VS Code, dass die Datei ein Python-Programm enthält.

## 4. Den ersten Python-Code schreiben

Tippe diesen Code im Editor ab:

```python
print("Hallo Python!")
```

Achte besonders auf:

- die runden Klammern,
- die Anführungszeichen,
- die genaue Schreibweise von `print`.

## 5. Datei speichern

Speichere dein Programm mit:

| Betriebssystem | Tastenkombination |
| -------------- | ----------------- |
| Windows        | `Ctrl + S`        |
| macOS          | `Cmd + S`         |

Ein weisser Punkt neben dem Dateinamen bedeutet, dass die Datei noch nicht gespeichert wurde.

## 6. Python-Interpreter auswählen

Der **Interpreter** ist das Programm, das deinen Python-Code ausführt.

1. Öffne die Befehlspalette mit `Ctrl` + `Shift` + `P` beziehungsweise `Cmd` + `Shift` + `P`.
2. Suche nach `Python: Select Interpreter`.
3. Wähle die installierte Python-3-Version aus.

Häufig zeigt VS Code die gewählte Version danach unten in der Statusleiste an.

## 7. Programm starten

Klicke oben rechts auf:

```text
▶ Python-Datei ausführen
```

VS Code öffnet unten ein Terminal. Dort sollte diese Ausgabe erscheinen:

```text
Hallo Python!
```

> **Merksatz:** Oben im Editor schreibst du das Programm. Unten im Terminal siehst du, was das Programm macht.

---

## Der Programmierkreislauf

Beim Programmieren wiederholst du immer denselben Ablauf:

1. Code schreiben
2. Datei speichern
3. Programm starten
4. Ausgabe prüfen
5. Code verbessern

> **Schreiben – speichern – starten – prüfen – verbessern.**

---

## Übung: Dein Name

### Erst überlegen

- Wo soll das Programm auf deinen Namen warten?
- Wie kann es sich die Eingabe merken?
- Was sollte sich ändern, wenn jemand anderes das Programm startet?

### Dein Programm

Ersetze den bisherigen Code in `hallo.py` durch dieses vollständige Programm. Es entspricht der Vorlage `beispiele/hallo.py` im Kursprojekt:

```python
name = input("Wie heisst du? ")
print("Hallo", name)
```

Führe danach folgende Schritte aus:

- [ ] Programm speichern
- [ ] Programm starten
- [ ] Im Terminal deinen Namen eingeben
- [ ] Mit Enter bestätigen
- [ ] Ausgabe überprüfen

Eine mögliche Ausgabe sieht so aus:

```text
Wie heisst du? Alex
Hallo Alex
```

Bei `input()` wartet Python auf eine Eingabe. Klicke dazu zuerst in das Terminal, gib deine Antwort ein und drücke **Enter**. Verwende das **Terminal**, nicht das Fenster **Output/Ausgabe**.

### Was geschieht hier?

| Code              | Bedeutung                                        |
| ----------------- | ------------------------------------------------ |
| `input(...)`      | Zeigt eine Frage an und wartet auf eine Eingabe. |
| `name = ...`      | Speichert die Eingabe in der Variable `name`.    |
| `print(...)`      | Gibt Text im Terminal aus.                       |
| `print("Hallo", name)` | Gibt die Begrüssung und den Namen mit einem Leerzeichen dazwischen aus. |

### Teste dein Programm

Starte die Datei nochmals und gib einen anderen Namen ein. Passt sich die Begrüssung an? Prüfe auch einen Namen mit Leerzeichen, zum Beispiel `Anna Maria`. Erkläre anschliessend, welche Zeile die Eingabe speichert und welche sie ausgibt.

---

## Wenn etwas nicht funktioniert

### VS Code zeigt «Select Interpreter»

Öffne die Befehlspalette und wähle über **Python: Select Interpreter** deine Python-3-Installation aus.

### Die Run-Schaltfläche fehlt

Kontrolliere:

- Ist die Datei mit `.py` gespeichert?
- Ist die Erweiterung **Python von Microsoft** installiert?
- Wurde ein Python-Interpreter ausgewählt?

### Das Programm startet nicht

Prüfe:

- Endet der Dateiname auf `.py`?
- Wurde die Datei gespeichert?
- Ist die richtige Datei im Editor geöffnet?
- Hast du `▶ Python-Datei ausführen` verwendet?

### Ich kann meinen Code im Terminal nicht bearbeiten

Das Terminal zeigt die Ausgabe des Programms. Bearbeite den Programmcode oben im Editor.

### VS Code wartet und macht nichts

Enthält dein Programm `input()`, wartet Python auf deine Eingabe. Klicke in das Terminal, gib etwas ein und drücke **Enter**.

### Die falsche Datei wird ausgeführt

Klicke vor dem Start im Editor auf die Python-Datei, die du ausführen möchtest.

### Es erscheint eine rote Fehlermeldung

Eine Fehlermeldung bedeutet nicht, dass du nicht programmieren kannst. Sie ist eine Nachricht von Python und hilft dir, den Fehler zu finden.

1. Lies zuerst die letzte Zeile der Fehlermeldung.
2. Suche nach einer angegebenen Zeilennummer.
3. Kontrolliere in dieser Zeile Klammern, Anführungszeichen und Schreibweise.

---

## Das solltest du jetzt können

Die Häkchen dienen zur Kontrolle und werden nach dem Neuladen nicht gespeichert.

- [ ] Ich kann meinen Kursordner öffnen.
- [ ] Ich kann eine `.py`-Datei erstellen.
- [ ] Ich kann Python-Code schreiben und speichern.
- [ ] Ich kann den Python-Interpreter auswählen.
- [ ] Mein erstes Programm hat `Hallo Python!` ausgegeben.
- [ ] Mein Programm mit `input()` kann meinen Namen einlesen.
- [ ] Ich kenne den Unterschied zwischen Editor und Terminal.
- [ ] Ich kann eine einfache Fehlermeldung untersuchen.

Wenn du alle Punkte abhaken kannst, startest du mit den [Mini-Games](mini-games/index.md).

Möchtest du Eingaben vorher noch etwas üben? Löse die freiwillige [Zusatzübung Begrüssung](aufgaben/aufgabe-01.md).
