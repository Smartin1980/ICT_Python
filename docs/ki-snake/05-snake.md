# 5. Ein vollständiges Snake

Diese Etappe ist für die Fortsetzung nach den ersten 120 Minuten gedacht. Arbeite in kleinen Schritten und verwende die KI jeweils nur für die aktuelle Teilaufgabe.

## Ziel und Spielregeln

Die Schlange startet mit drei Körperfeldern und bewegt sich nach rechts. Goldfarbenes Futter bringt einen Punkt und ein zusätzliches Körperfeld. Wand- oder Selbstkollision führt zu Game Over. Eine direkte Kehrtwende ist verboten. Nach dem Ende startet R neu; Esc beendet das Programm. Punkte stehen im Fenstertitel. Wenn die Schlange das ganze Feld füllt, gewinnt sie.

## Neue Werkzeuge verstehen

| Ausdruck | Bedeutung |
| --- | --- |
| `[(5, 8), (4, 8), (3, 8)]` | Liste von Positionen: Kopf zuerst, Schwanz zuletzt |
| `schlange[0]` | Position des Kopfes |
| `[kopf] + schlange` | Neuen Kopf vorne anfügen |
| `schlange.pop()` | Letztes Körperfeld entfernen |
| `schlange[:-1]` | Alle Körperfelder ausser der letzten Schwanzspitze |
| `kopf in koerper` | Prüfen, ob die Position bereits belegt ist |
| `None` | Hier: Es gibt kein freies Feld für Futter mehr |

Eine Funktion kann mehrere Werte zurückgeben. `schlange, richtung, futter, punkte, status = neue_runde()` verteilt die fünf zurückgegebenen Werte auf fünf Namen. Der Status ist ein Text: `"spiel"`, `"verloren"` oder `"gewonnen"`.

## Erst überlegen

- Wie bleibt die Länge bei einer normalen Bewegung gleich?
- Welche Zeile musst du beim Fressen überspringen, damit die Schlange wächst?
- Warum darf Futter nicht innerhalb der Schlange erscheinen?
- Was passiert, wenn du innerhalb desselben Bewegungsschritts erst nach oben und dann nach links lenkst, obwohl du zuvor nach rechts gefahren bist?

## Bauauftrag in Etappen

Erstelle `03_snake.py` als neue Datei. Die Grafikgrundlagen kennst du schon. Die Lösung unten ist vollständig und benötigt keine andere Spieldatei.

1. **Körper:** Ersetze die einzelne Kopfposition durch eine Liste. Zeichne alle Körperfelder in einer Schleife. Füge pro Schritt vorne einen Kopf hinzu und entferne hinten ein Feld.
2. **Futter:** Schreibe `neues_futter(schlange)`. Sammle mit zwei Schleifen alle freien Rasterpositionen in einer Liste und wähle daraus zufällig eine Position.
3. **Wachstum:** Prüfe, ob der neue Kopf auf dem Futter landet. Dann entfernst du den Schwanz nicht, erhöhst die Punkte und erzeugst neues Futter.
4. **Spielende:** Eine Position ausserhalb des Rasters oder im verbleibenden Körper setzt den Status auf `"verloren"`. Zeichnen und Ereignisverarbeitung laufen weiter, die Bewegung stoppt.
5. **Steuerung:** Verhindere die direkte Gegenrichtung. Lasse mit `gedreht` höchstens eine Richtungsänderung zwischen zwei Schritten zu.
6. **Neustart:** Verpacke Startkörper, Richtung, Futter, Punkte und Status in `neue_runde()`. R ruft die Funktion nach dem Spielende erneut auf.

## KI-Aufträge für einzelne Etappen

```text
Erkläre mir an drei Rasterpositionen, wie eine Snake-Liste einen Schritt
weiterwandert. Zeige zuerst die Liste vorher und nachher, noch kein Pygame.
```

```text
Prüfe meine Funktion neues_futter. Futter darf nur auf einem freien
Rasterfeld erscheinen. Was soll geschehen, wenn alle Felder belegt sind?
Gib zuerst einen Hinweis. Hier ist meine Funktion: [Code einfügen]
```

```text
Hier ist meine Kollisionserkennung: [Code einfügen]
Untersuche den Sonderfall, dass der Kopf auf die alte Schwanzspitze zieht,
die im selben Schritt verschwindet. Erkläre, wann das erlaubt ist.
```

## Tipps zu den schwierigen Stellen

Ohne Futter verschwindet der Schwanz im selben Schritt. Deshalb ist die alte Schwanzposition dann kein Hindernis: Prüfe gegen `schlange[:-1]`. Beim Fressen bleibt der Schwanz und zählt mit. Die Lösung berechnet einen Schritt in einer eigenen Funktion; so lassen sich die Regeln ohne Spielfenster prüfen.

`gedreht` wird vor dem Abholen der Ereignisse auf `False` gesetzt. Nach einer erlaubten Drehung wird es `True`. So können schnelle Tastendrücke keine indirekte Kehrtwende im selben Schritt auslösen. Dieser einfache Schutz ignoriert weitere Drehungen bis zum nächsten Schritt.

Wenn keine freie Futterposition mehr existiert, liefert `neues_futter()` den Wert `None`. Dadurch wird das Spiel gewonnen und sucht nicht endlos nach Futter.

## Teste dein Spiel

| Test | Erwartung |
| --- | --- |
| Start | Drei Körperfelder, 0 Punkte, Bewegung nach rechts |
| Direkt links drücken | Gegenrichtung wird ignoriert |
| Futter einsammeln | Länge und Punkte steigen um 1; neues Futter liegt frei |
| Jede der vier Wände anfahren | Game Over, keine weitere Bewegung |
| Mit längerer Schlange in den eigenen Körper lenken | Game Over |
| Nach Game Over R drücken | Drei Körperfelder, 0 Punkte, neue Runde |
| Esc / Schliessen, auch nach Game Over | Programm beendet sich |

Für reproduzierbare Tests kannst du in einer **Testkopie** das erste Futter auf `(6, 8)` setzen: Es liegt direkt vor dem Startkopf. Verändere im Original danach nichts dauerhaft. Weitere Grenztests und die Python-Prüfdatei sind im [Lehrpersonenplan](lehrpersonen.md) beschrieben.

## Vollständiger Lösungscode

Datei: `beispiele/snake/03_snake.py`. Dieses Grundspiel enthält alle oben beschriebenen Regeln. Kreative Erweiterungen folgen erst danach.

<!-- CODE:03_snake.py -->
```python
"""Einfaches Snake: Pfeiltasten, Futter, Punkte, Kollision und Neustart."""
import random
import pygame

ZELLE = 25
SPALTEN = 24
ZEILEN = 18
TEMPO = 8


def neues_futter(schlange):
    freie_felder = []
    for y in range(ZEILEN):
        for x in range(SPALTEN):
            if (x, y) not in schlange:
                freie_felder.append((x, y))
    if not freie_felder:
        return None  # Alle Felder belegt: gewonnen!
    return random.choice(freie_felder)


def neue_runde():
    schlange = [(5, 8), (4, 8), (3, 8)]
    richtung = (1, 0)
    return schlange, richtung, neues_futter(schlange), 0, "spiel"


def waehle_richtung(richtung, wunsch):
    # Eine direkte Umkehr würde den Kopf in den eigenen Hals bewegen.
    if wunsch == (-richtung[0], -richtung[1]):
        return richtung
    return wunsch


def schritt(schlange, richtung, futter, punkte):
    kopf_x, kopf_y = schlange[0]
    dx, dy = richtung
    kopf = (kopf_x + dx, kopf_y + dy)
    x, y = kopf
    if not (0 <= x < SPALTEN and 0 <= y < ZEILEN):
        return schlange, futter, punkte, "verloren"

    frisst = kopf == futter
    # Ohne Futter verschwindet die Schwanzspitze im selben Schritt.
    koerper = schlange if frisst else schlange[:-1]
    if kopf in koerper:
        return schlange, futter, punkte, "verloren"

    schlange = [kopf] + schlange
    if frisst:
        punkte = punkte + 1
        futter = neues_futter(schlange)
    else:
        schlange.pop()

    if futter is None:
        return schlange, futter, punkte, "gewonnen"
    return schlange, futter, punkte, "spiel"


def main():
    pygame.init()
    fenster = pygame.display.set_mode((SPALTEN * ZELLE, ZEILEN * ZELLE))
    schrift = pygame.font.Font(None, 32)
    uhr = pygame.time.Clock()
    schlange, richtung, futter, punkte, status = neue_runde()
    laeuft = True

    while laeuft:
        # Höchstens eine Richtungsänderung zwischen zwei Schritten zulassen.
        gedreht = False
        for ereignis in pygame.event.get():
            if ereignis.type == pygame.QUIT:
                laeuft = False
            elif ereignis.type == pygame.KEYDOWN:
                if ereignis.key == pygame.K_ESCAPE:
                    laeuft = False
                elif ereignis.key == pygame.K_r and status != "spiel":
                    schlange, richtung, futter, punkte, status = neue_runde()
                    gedreht = True
                elif status == "spiel" and not gedreht:
                    wunsch = richtung
                    if ereignis.key == pygame.K_UP:
                        wunsch = (0, -1)
                    elif ereignis.key == pygame.K_DOWN:
                        wunsch = (0, 1)
                    elif ereignis.key == pygame.K_LEFT:
                        wunsch = (-1, 0)
                    elif ereignis.key == pygame.K_RIGHT:
                        wunsch = (1, 0)
                    neue_richtung = waehle_richtung(richtung, wunsch)
                    if neue_richtung != richtung:
                        richtung = neue_richtung
                        gedreht = True

        if not laeuft:
            break
        if status == "spiel":
            schlange, futter, punkte, status = schritt(schlange, richtung, futter, punkte)

        fenster.fill((20, 25, 35))
        if futter is not None:
            x, y = futter
            pygame.draw.rect(fenster, (255, 190, 60), (x * ZELLE, y * ZELLE, ZELLE, ZELLE))
        for x, y in schlange:
            pygame.draw.rect(fenster, (80, 220, 120), (x * ZELLE, y * ZELLE, ZELLE - 1, ZELLE - 1))

        pygame.display.set_caption("Snake | Punkte: " + str(punkte) + " | Pfeiltasten | Esc: Ende")
        if status != "spiel":
            meldung = "Gewonnen!" if status == "gewonnen" else "Game Over!"
            text = schrift.render(meldung + "  R: Neustart", True, (255, 255, 255))
            position = text.get_rect(center=(SPALTEN * ZELLE // 2, ZEILEN * ZELLE // 2))
            pygame.draw.rect(fenster, (20, 25, 35), position.inflate(20, 20))
            fenster.blit(text, position)
        pygame.display.flip()
        uhr.tick(TEMPO)

    pygame.quit()


if __name__ == "__main__":
    main()
```
<!-- END CODE -->

[Weiter: Testen und kreativ weiterbauen](06-weiterbauen.md)
