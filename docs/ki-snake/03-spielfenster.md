# 3. Mein erstes Spielfenster

## Ziel und neue Werkzeuge

Du verstehst den Ablauf **Ereignisse → Zeichnen → Anzeigen → Tempo begrenzen**. Dies wird in einer Spielschleife wiederholt. Im Unterschied zu unseren Textspielen wartet die Schleife nicht auf `input()`.

| Code | Bedeutung |
| --- | --- |
| `pygame.init()` | Pygame vorbereiten |
| `display.set_mode((600, 450))` | Ein Fenster mit Breite und Höhe in Pixeln öffnen |
| `event.get()` | Ereignisse wie Tastendruck oder Schliessen abholen |
| `fenster.fill(...)` | Den Hintergrund vor jedem Bild neu zeichnen |
| `draw.rect(...)` | Ein Rechteck mit Position und Grösse zeichnen |
| `display.flip()` | Das fertig gezeichnete Bild anzeigen |
| `uhr.tick(30)` | Die Schleife auf höchstens 30 Durchläufe pro Sekunde begrenzen |

### Pixel und Raster

Oben links ist `(0, 0)`. x wächst nach rechts, y nach unten. Unser Feld besteht aus 24 Spalten und 18 Zeilen, eine Zelle ist 25 Pixel breit und hoch. Rasterposition `(5, 8)` wird zu Pixelposition `(125, 200)`. Wir speichern später Rasterkoordinaten und multiplizieren erst beim Zeichnen mit `ZELLE`.

`(5, 8)` ist ein **Tupel**, ein festes Wertepaar. `x, y = 5, 8` weist zwei Werte zu. Farben sind Dreiergruppen für Rot, Grün und Blau, jeweils von 0 bis 255. Grosse Variablennamen wie `ZELLE` kennzeichnen hier Einstellungen, die während einer Runde gleich bleiben.

## Erst überlegen

- Wie breit ist das Fenster: 24 oder 600 Pixel?
- Was passiert bei Rasterposition `(0, 0)`?
- Warum muss auch ein unbewegtes Spiel Ereignisse verarbeiten?

## Bauauftrag

1. Erstelle `01_spielfenster.py` mit dem vollständigen Startcode unten. Diesen Rahmen darfst du übernehmen.
2. Finde Ereignisverarbeitung, Zeichnen und Anzeige im Code.
3. Sage voraus, wo das Quadrat bei `(10, 4)` erscheint, und ändere die Rasterposition.
4. Ändere eine Farbe und starte neu.

## KI als Erklärhilfe

```text
Erkläre mir in diesem Pygame-Code die vier Argumente des Rechtecks:
(5 * ZELLE, 8 * ZELLE, ZELLE, ZELLE).
ZELLE ist 25. Nenne die Pixelposition und Grösse. Ändere den Code noch nicht.
```

## Tipps

Die Funktion `main()` enthält den Programmablauf. `if __name__ == "__main__":` startet sie, wenn du diese Datei ausführst. Beim Importieren für Prüfungen startet dadurch kein Fenster. Du musst diese beiden Rahmenzeilen zunächst nur wiedererkennen können.

## Teste dich

- Erwartet: Fenster 600 × 450 Pixel, grünes Quadrat 25 × 25 Pixel bei `(125, 200)`.
- Nach der Änderung auf `(10, 4)`: Quadrat bei `(250, 100)`.
- Sowohl Fensterschliessen als auch Esc müssen das Programm beenden.

Quellen: [Pygame-Ereignisse](https://www.pygame.org/docs/ref/event.html), [Clock.tick](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick).

## Vollständiger Lösungscode

Datei: `beispiele/snake/01_spielfenster.py`. Enthält den ursprünglichen Startzustand vor deinen Farb- und Positionsänderungen.

<!-- CODE:01_spielfenster.py -->
```python
"""Etappe 1: Ein Fenster und ein Schlangenkopf auf einem Raster."""
import pygame

ZELLE = 25
SPALTEN = 24
ZEILEN = 18


def main():
    pygame.init()
    fenster = pygame.display.set_mode((SPALTEN * ZELLE, ZEILEN * ZELLE))
    pygame.display.set_caption("Snake – mein erstes Fenster")
    uhr = pygame.time.Clock()
    laeuft = True

    while laeuft:
        # Ereignisse abholen, damit das Fenster auf Eingaben reagiert.
        for ereignis in pygame.event.get():
            if ereignis.type == pygame.QUIT:
                laeuft = False
            elif ereignis.type == pygame.KEYDOWN:
                if ereignis.key == pygame.K_ESCAPE:
                    laeuft = False

        fenster.fill((20, 25, 35))
        pygame.draw.rect(fenster, (80, 220, 120), (5 * ZELLE, 8 * ZELLE, ZELLE, ZELLE))
        pygame.display.flip()
        uhr.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
```
<!-- END CODE -->

[Weiter: Bewegung mit KI](04-bewegung.md)
