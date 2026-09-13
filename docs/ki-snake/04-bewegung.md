# 4. Bewegung mit KI entwickeln

## Ziel

Ein Schlangenkopf bewegt sich selbstständig auf dem Raster. Pfeiltasten ändern die Richtung. Am Rand bleibt er stehen, bis du wieder in eine gültige Richtung lenkst. Futter und Körper folgen erst im nächsten Kapitel.

## Das neue Werkzeug: Richtung als Wertepaar

| Richtung | `(dx, dy)` |
| --- | --- |
| Rechts | `(1, 0)` |
| Links | `(-1, 0)` |
| Oben | `(0, -1)` |
| Unten | `(0, 1)` |

Ein Schritt berechnet `neu_x = x + dx` und `neu_y = y + dy`. Ein Rasterfeld pro Schleifendurchlauf und `uhr.tick(8)` bedeuten höchstens acht Schritte pro Sekunde. Zeichnung und Bewegung haben hier absichtlich dasselbe Tempo.

## Erst überlegen

- Wo steht der Kopf nach drei Schritten von `(5, 8)` in Richtung `(1, 0)`?
- Welche x-Werte sind in 24 Spalten erlaubt?
- Warum bewegt sich der Kopf nach einem einzelnen Tastendruck weiter?

## Bauauftrag in kleinen Schritten

1. Kopiere deine erste Datei nach `02_bewegung.py`.
2. Speichere `x, y = 5, 8` und `dx, dy = 1, 0` vor der Schleife.
3. Verwende x und y beim Zeichnen. Ergänze pro Durchlauf einen Bewegungsschritt und setze das Tempo auf 8.
4. Ergänze in der Ereignisverarbeitung die vier Pfeiltasten und ihre Richtungen.
5. Prüfe vor der Bewegung, ob die nächste Position im Raster liegt. Nur dann übernimmst du sie.

Für die erste Doppelstunde darfst du den vollständigen Code unten als funktionierenden Ausgangspunkt verwenden und die folgende KI-Aufgabe bearbeiten. Der Bauauftrag von Grund auf ist für die Fortsetzung gedacht.

## Erste KI-Änderung: Wandkontakt sichtbar machen

Die Figur soll **rot** erscheinen, solange ihr nächster Schritt aus dem Spielfeld führen würde. Bei einer gültigen Richtung wird sie wieder grün. Alle bisherigen Funktionen bleiben erhalten.

```text
Ich lerne Python und kenne Variablen, if/else, Schleifen und Funktionen.
Mein Pygame-Kopf hält bereits am Rand. Er soll bei einem blockierten Schritt
rot und bei einem erlaubten Schritt grün sein. Keine neuen Bibliotheken.
Erkläre zuerst, wo die Farbe festgelegt werden muss. Zeige dann nur die
nötigen Änderungen mit ihrer Einfügestelle und nenne vier Randtests.
Hier ist mein vollständiger aktueller Code:
[Code aus 02_bewegung.py einfügen]
```

Speichere deine Änderung als `02_bewegung_eigen.py`. Lies den Vorschlag, bevor du ihn übernimmst. Notiere Prompt, Änderung und Tests im [Lernprotokoll](06-weiterbauen.md#mein-lernprotokoll).

## Tipps ohne KI

Lege die Farbe in jedem Durchlauf passend zur vorhandenen Randprüfung fest. Bei einer erlaubten Bewegung verwendest du Grün, im `else`-Zweig Rot. Übergib diese Farbvariable an `pygame.draw.rect`. Setze sie nicht nur einmal vor der Schleife, sonst kann die Farbe nicht passend wechseln.

## Teste dein Programm

| Situation | Grundspiel | Eigene Farbänderung |
| --- | --- | --- |
| Nach rechts bis x = 23 | Bleibt sichtbar stehen | Wird rot |
| Nach links bis x = 0 | Bleibt sichtbar stehen | Wird rot |
| Nach oben bis y = 0 | Bleibt sichtbar stehen | Wird rot |
| Nach unten bis y = 17 | Bleibt sichtbar stehen | Wird rot |
| Vom Rand weglenken | Bewegt sich wieder | Wird grün |
| Esc / Fenster schliessen | Beendet das Programm | Funktioniert weiterhin |

In dieser Etappe sind Kehrtwenden noch erlaubt, weil es keinen Körper gibt. Eine reine Farbänderung gilt erst als fertig, wenn du sie erklären und die Tests zeigen kannst.

## Vollständiger Lösungscode

Datei: `beispiele/snake/02_bewegung.py`. Die kreative Farbänderung ist eine eigene Aufgabe und noch nicht eingebaut.

<!-- CODE:02_bewegung.py -->
```python
"""Etappe 2: Automatische Bewegung; an der Wand bleibt der Kopf stehen."""
import pygame

ZELLE = 25
SPALTEN = 24
ZEILEN = 18
TEMPO = 8


def main():
    pygame.init()
    fenster = pygame.display.set_mode((SPALTEN * ZELLE, ZEILEN * ZELLE))
    pygame.display.set_caption("Snake – Bewegung mit Pfeiltasten")
    uhr = pygame.time.Clock()
    x, y = 5, 8
    dx, dy = 1, 0
    laeuft = True

    while laeuft:
        for ereignis in pygame.event.get():
            if ereignis.type == pygame.QUIT:
                laeuft = False
            elif ereignis.type == pygame.KEYDOWN:
                if ereignis.key == pygame.K_ESCAPE:
                    laeuft = False
                elif ereignis.key == pygame.K_UP:
                    dx, dy = 0, -1
                elif ereignis.key == pygame.K_DOWN:
                    dx, dy = 0, 1
                elif ereignis.key == pygame.K_LEFT:
                    dx, dy = -1, 0
                elif ereignis.key == pygame.K_RIGHT:
                    dx, dy = 1, 0

        neu_x = x + dx
        neu_y = y + dy
        # Erst prüfen, dann bewegen. Randfelder sind noch gültig.
        if 0 <= neu_x < SPALTEN and 0 <= neu_y < ZEILEN:
            x, y = neu_x, neu_y

        fenster.fill((20, 25, 35))
        pygame.draw.rect(fenster, (80, 220, 120), (x * ZELLE, y * ZELLE, ZELLE, ZELLE))
        pygame.display.flip()
        # Ein Feld pro Bild: höchstens acht Schritte pro Sekunde.
        uhr.tick(TEMPO)

    pygame.quit()


if __name__ == "__main__":
    main()
```
<!-- END CODE -->

[Weiter: Ein vollständiges Snake](05-snake.md)
