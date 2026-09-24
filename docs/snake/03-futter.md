# 🍎 Schritt 3 – Futter

## Ziel · ca. 15 Minuten

Ein rotes Futterquadrat erscheint zufällig auf dem Raster.

## 🏗️ Erst planen

Futter braucht eine freie Rasterzelle. Die linke obere Ecke darf bei x von 0 bis 780 und bei y von 0 bis 580 liegen – jeweils in 20er-Schritten.

## 🤖 Prompt 3

```text
Die Bewegung und Steuerung funktionieren.

Jetzt braucht Snake Futter.
Wir verwenden weiterhin Python und Pygame Zero.

Anforderungen:

- Futter als rotes Quadrat mit 20 × 20 Pixeln
- genau auf dem 20-Pixel-Raster und vollständig im Spielfeld
- zufällige Position
- beim Start genau ein Futter
- verwende Python random
- das Futter soll nicht auf der Schlange erscheinen
- das Futter bleibt an seiner Position
- Snake kann es noch nicht fressen

Verändere nur das, was notwendig ist.

Erkläre mir danach:

1. Wie wird die zufällige Position bestimmt?
2. Wofür verwenden wir random?
3. Wie verhindern wir, dass Futter auf Snake erscheint?
```

## ▶️ Checkpoint

Starte das Spiel mehrmals und prüfe die Positionen.

- [ ] Beim Start erscheint genau ein rotes Futterquadrat.
- [ ] Das Futter liegt genau auf dem Raster und vollständig im Fenster.
- [ ] Es erscheint nicht auf der Schlange.
- [ ] Bei mehreren Starts sehe ich unterschiedliche Positionen. Eine Wiederholung ist erlaubt.
- [ ] Wenn Snake über das Futter fährt, bleibt es liegen und Snake wächst noch nicht.

## 🧠 Das kenne ich schon

Im Mini-Game [Wörter raten – Listen](../mini-games/07-listen.md) hat `random.choice()` ein zufälliges Wort gewählt. Hier hilft `random`, eine zufällige Futterposition zu bestimmen.

Zeige im Code, wo geprüft wird, ob eine Position schon in der Liste `snake` vorkommt. Eine belegte Position darf nicht als neues Futter verwendet werden.

[Zurück](02-bewegung.md) · [Zur Übersicht](index.md) · [Weiter: Fressen und wachsen](04-wachsen.md)
