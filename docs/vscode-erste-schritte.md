---
layout: default
title: VS Code bedienen
nav_order: 2
description: Erste Schritte mit VS Code für den Python-Kurs
---

# Erste Schritte mit VS Code

VS Code ist unser **digitaler Arbeitsplatz zum Programmieren**. Ähnlich wie Word beim Schreiben von Texten hilft, unterstützt uns VS Code beim Schreiben von Programmen.

Für unseren Kurs brauchst du in VS Code zunächst nur wenige Funktionen.

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

Erstelle unter **Dokumente** einen neuen Ordner:

```text
Python-Kurs
```

Später kann dieser Ordner beispielsweise so aufgebaut sein:

```text
Python-Kurs
├── 01_Grundlagen
├── 02_Beispiele
└── 03_Spiel
```

## 2. Kursordner in VS Code öffnen

1. Starte VS Code.
2. Wähle **Datei → Ordner öffnen**.
3. Wähle den Ordner `Python-Kurs` aus.
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
print("Hallo Welt!")
print("Mein erstes Python-Programm funktioniert.")
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

## 6. Programm starten

Klicke oben rechts auf:

```text
▶ Python-Datei ausführen
```

Im Terminal sollte diese Ausgabe erscheinen:

```text
Hallo Welt!
Mein erstes Python-Programm funktioniert.
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

Ersetze den bisherigen Code durch dieses Programm:

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

Bei `input()` wartet Python auf eine Eingabe. Klicke dazu zuerst in das Terminal, gib deine Antwort ein und drücke **Enter**.

---

## Wenn etwas nicht funktioniert

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

- [ ] Ich kann meinen Kursordner öffnen.
- [ ] Ich kann eine `.py`-Datei erstellen.
- [ ] Ich kann Python-Code schreiben und speichern.
- [ ] Ich kann ein Programm starten.
- [ ] Ich kenne den Unterschied zwischen Editor und Terminal.
- [ ] Ich kann eine einfache Fehlermeldung untersuchen.

Wenn du alle Punkte abhaken kannst, bist du bereit für dein nächstes Python-Programm.
