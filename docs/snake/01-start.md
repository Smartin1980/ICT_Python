# 🐍 Schritt 1 – Unser erster Snake-Prototyp

## Ziel · ca. 20 Minuten

Am Ende sehen wir ein Spielfeld und eine Schlange aus **drei Segmenten**. Noch keine Bewegung.

## Vor dem Start

Nutze deine eingerichtete Umgebung aus [Python und VS Code installieren](../python-vscode-installation.md). Erstelle darin einen eigenen Ordner `snake` und öffne ihn in VS Code. Lege die Datei `snake.py` an.

Falls Pygame Zero noch fehlt, installiere es im Terminal von VS Code mit dem Python, das du auch für dein Spiel verwendest:

```text
python -m pip install pgzero
```

Das Paket heisst `pgzero`. Unser Code verwendet `import pgzrun` ganz oben und `pgzrun.go()` ganz unten. Damit lässt sich das Spiel als Python-Datei starten. Siehe auch die [offizielle Startanleitung für IDEs](https://pygame-zero.readthedocs.io/en/stable/ide-mode.html).

## 🏗️ Unser Plan: ein Raster

- Das Spielfeld ist **800 × 600 Pixel** gross.
- Eine Rasterzelle ist **20 × 20 Pixel** gross. Das ergibt 40 Spalten und 30 Zeilen.
- Die Schlange besteht aus Quadraten, die genau auf diesem Raster liegen.

Die Position bezeichnet jeweils die **linke obere Ecke** eines Quadrats. Links oben im Fenster liegt `(0, 0)`. Nach rechts wird die erste Zahl grösser, nach unten die zweite. Sichtbare Rasterlinien brauchen wir nicht.

## 🤖 Prompt 1

```text
Du bist mein Programmierassistent.

Wir entwickeln gemeinsam ein Snake-Spiel mit Python und Pygame Zero.

Ich bin der Architekt und entscheide, wie das Spiel funktioniert.

Erstelle unseren ersten Prototyp:

- Spielfeld: 800 × 600 Pixel
- dunkler Hintergrund
- Rastergrösse: 20 Pixel
- Schlange aus 3 grünen Quadraten
- Start ungefähr in der Mitte
- noch keine Bewegung
- noch kein Futter

Speichere die Positionen der Schlange in einer Liste, mit dem Kopf zuerst.
Eine Position ist die linke obere Ecke eines Quadrats in Pixeln.

Halte den Code möglichst einfach und für Python-Anfänger verständlich.
Nutze eine Datei snake.py ohne zusätzliche Bilddateien.
Verwende import pgzrun ganz oben und pgzrun.go() ganz unten,
damit ich die Datei mit python snake.py starten kann.

Erkläre mir danach kurz:

1. Warum verwenden wir für die Schlange eine Liste?
2. Was bedeutet eine Position wie (400, 300)?
```

## ▶️ Checkpoint

Übernimm den Code in `snake.py` und speichere. Öffne das Terminal im Ordner mit der Datei und starte:

```text
python snake.py
```

- [ ] Das Fenster startet.
- [ ] Ich sehe drei grüne Snake-Segmente auf dunklem Hintergrund.
- [ ] Die Schlange steht still.
- [ ] Es gibt keine Fehlermeldung.

Schliesse das Spielfenster vor jedem erneuten Start.

## 🧠 Das kenne ich schon

Im Mini-Game [Wörter raten – Listen](../mini-games/07-listen.md) hast du mehrere Wörter in einer Liste gespeichert. Hier speichert die Liste mehrere Positionen:

```python
snake = [(400, 300), (380, 300), (360, 300)]
```

Jedes Zahlenpaar ist eine Koordinate: `(400, 300)` bedeutet 400 Pixel von links und 300 Pixel von oben. Ein solches Zahlenpaar heisst **Tupel**. `snake[0]` ist die Position des Kopfes. Die weiteren Einträge sind die Körpersegmente.

[Zur Übersicht](index.md) · [Weiter: Bewegung und Steuerung](02-bewegung.md)
