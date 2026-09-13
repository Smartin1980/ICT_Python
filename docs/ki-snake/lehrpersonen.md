# Lehrpersonen: KI & Snake

## Rahmen und Lernziele

Zielgruppe: 14–16 Jahre, Python-Grundlagen aus den Mini-Games. Umgebung: vorhandenes Python und VS Code, Pygame, freigegebener KI-Textchat im Browser. Keine Editor-Agenten oder API-Schlüssel erforderlich.

Nach den **ersten 120 Minuten inklusive 10 Minuten Pause** können die SuS eine Grenze von KI benennen, einen konkreten Prompt formulieren, das Pygame-Fenster ausführen und eine kleine Änderung erklären und testen. Das vollständige Snake ist Material für eine **anschliessende Einheit von etwa 90–120 Minuten**, kein Pflichtziel der ersten zwei Stunden.

## Vor der Stunde

- Installation mit dem tatsächlichen Schülergerät und Schulnetz testen: `.venv`, Paketinstallation, Interpreterwahl, Fensterstart und Tastatur.
- Eine auf den Schulgeräten funktionierende Python-Version festlegen. Das Material wurde mit Python 3.11 und Pygame 2.6.1 geprüft; keine automatische Kompatibilitätszusage für jede neue Python-Version.
- Die drei Dateien unter `beispiele/snake` und das Lernprotokoll vorab verteilen oder über die Lernseiten bereitstellen.
- Freigegebene KI-Zugänge, Altersbedingungen und nötige Einwilligungen vorab mit der Schule klären. Niemand muss spontan ein privates Konto eröffnen oder Zugangsdaten teilen.
- Für fehlenden Zugang, Nutzungslimits oder Netzprobleme die vorbereiteten Hinweise dieser Seiten und den Code lokal bereithalten. Partnerarbeit an einem erlaubten Zugang oder eine Lehrperson-Demo ermöglichen dieselbe Lernaufgabe.
- Snake Advanced nur kurz als späteren Kreativausblick zeigen; für die ersten Schritte die einfache Version verwenden.

## Ablauf: 120 Minuten

| Minuten | Aktivität | Material / Ergebnis |
| --- | --- | --- |
| 0–10 | Einfaches Snake zeigen, Spielregeln sammeln | `03_snake.py`; Was muss das Programm speichern? |
| 10–25 | KI-Theorie und Regeln diskutieren | [KI verstehen](01-ki-verstehen.md); ein Beispiel für einen plausiblen Fehler |
| 25–40 | Raster und Spielschleife an der Tafel | [Spielfenster](03-spielfenster.md); Raster- in Pixelposition umrechnen |
| 40–50 | «Mach Snake» gemeinsam verbessern; falsche Randprüfung untersuchen | Prompt mit Ziel, Kontext und gewünschter Hilfe |
| 50–60 | Pause | |
| 60–80 | Umgebung einrichten, Chat oder Alternative bereitstellen | [Setup](02-setup.md); Fenster startet und schliesst |
| 80–90 | Startcode lesen, Position oder Farbe ändern | `01_spielfenster.py`; Vorhersage und Beobachtung |
| 90–105 | Etappe 2 öffnen; Randfarbe mit KI oder Hilfekarte ergänzen | [Bewegung](04-bewegung.md); `02_bewegung_eigen.py` |
| 105–115 | Vier Ränder testen, eine Zeile dem Partner erklären | Lernprotokoll mit Erwartung und Ergebnis |
| 115–120 | Exit-Ticket | «Mein Test», «Meine Erklärung», «Meine offene Frage» |

Bei Setup-Verzögerungen endet das Pflichtziel nach Etappe 1 mit einer Farbänderung und einem nachvollziehbaren Test. Die Randaufgabe verschiebt sich in die nächste Stunde. Schnelle Gruppen untersuchen die Körperliste, ohne den gemeinsamen Reflexionsteil auszulassen.

## Fortsetzung: einfaches Snake

Vorschlag für weitere 90 Minuten: 10 Minuten Rückblick, 20 Minuten Körperliste, 20 Minuten Futter/Wachstum, 20 Minuten Kollision/Neustart, 15 Minuten Partnerprüfung, 5 Minuten Dokumentation. Bei Bedarf zusätzliche 30 Minuten zum Lesen und Erklären des Codes einplanen. Die vollständige Lösung ist auf [Etappe 5](05-snake.md) verfügbar. SuS müssen nicht alle Pygame-Befehle auswendig reproduzieren.

## Vorbereitete Hilfekarte: Farbänderung ohne KI-Zugang

Frage zuerst: «Wo entscheidet dein Programm bereits, ob eine Bewegung erlaubt ist?» Die Farbe muss in beiden Zweigen dieser Entscheidung gesetzt werden. Der passende Ausschnitt ist:

```python
if 0 <= neu_x < SPALTEN and 0 <= neu_y < ZEILEN:
    x, y = neu_x, neu_y
    farbe = (80, 220, 120)
else:
    farbe = (240, 70, 70)
```

Danach im vorhandenen `pygame.draw.rect` den bisherigen Farbwert durch `farbe` ersetzen. Das ist ein Ausschnitt für Etappe 2, kein eigenständig startbares Programm. Test: alle vier Ränder, vom Rand weglenken und Esc. Erwartet: rot bei blockiertem Schritt, grün bei erlaubtem Schritt.

## Lösungshinweise für Denkfragen

- Fenster: 24 × 25 = 600 Pixel breit. `(10, 4)` entspricht `(250, 100)` Pixeln. Ereignisse sind auch zum Schliessen nötig.
- Bewegung: Nach drei Schritten von `(5, 8)` nach rechts steht der Kopf bei `(8, 8)`. Gültige Spalten sind 0–23. Die Richtung bleibt zwischen Tastendrücken gespeichert.
- Körper: Vorne einen Kopf anfügen, hinten ein Feld entfernen; beim Fressen das Entfernen auslassen.
- Selbstkollision: Die im selben Schritt verschwindende Schwanzspitze darf betreten werden. Das übrige Körperstück ist ein Hindernis.
- Steuerung: Rechts → oben → links vor dem nächsten Schritt wäre trotz einzelner erlaubter Drehungen eine indirekte Umkehr. Nur eine Drehung pro Schritt zulassen.
- Volles Feld: Kein freies Futterfeld bedeutet Sieg statt einer endlosen Zufallssuche.

## Prüfungen und Beurteilung

Die Prüfsuite `tests/test_snake.py` kontrolliert Spielregeln und startet alle drei Programme mit einem unsichtbaren SDL-Testfenster. Aus dem **Repository-Hauptordner**, mit einem Python mit installiertem Pygame:

```text
python -m unittest discover -s tests -p test_snake.py
```

Zusätzlich vor Ort prüfen: sichtbare Darstellung, Fensterfokus, vier Richtungen, Game Over, R und Esc. Automatische Tests ersetzen den Test auf Schulgeräten nicht.

| Kriterium | Erfüllt, wenn … |
| --- | --- |
| Auftrag | Eine kleine Änderung und klare Grenzen formuliert sind |
| Verständnis | Mindestens eine relevante Zeile korrekt erklärt wird |
| Prüfung | Normalfall, Grenzfall und bisherige Funktion dokumentiert sind |
| Transparenz | Übernommene und verworfene KI-Hilfe benannt wird |

Bewerte das Vorgehen und Verständnis, nicht die Länge der KI-Antwort oder die Menge neuer Features. Ein nicht gelöster Fehler mit sauberem Testprotokoll ist ein sinnvoller Lernstand.

## Quellen und Pflege

Offizielle technische Quellen: [Pygame](https://www.pygame.org/docs/), [Ereignisse](https://www.pygame.org/docs/ref/event.html), [Zeitsteuerung](https://www.pygame.org/docs/ref/time.html). Für didaktische Anregungen: [OpenAI: Bildung](https://learn.chatgpt.com/use-cases/collections/education). Anbieterbedingungen und schulische Vorgaben vor jedem Durchlauf erneut prüfen; dieses Material setzt keinen bestimmten Modellnamen oder ein festes Nachrichtenkontingent voraus.

Nach Änderungen an den Python-Dateien synchronisiert `python scripts/sync_snake_docs.py` die vollständigen Codeblöcke und das Downloadpaket. `python scripts/sync_snake_docs.py --check` prüft, ob sie aktuell sind.
