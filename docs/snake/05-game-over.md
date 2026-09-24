# 💥 Schritt 5 – Game Over

## Ziel · ca. 20 Minuten

Snake stoppt, wenn der Kopf das Spielfeld verlässt oder den eigenen Körper berührt.

## 🏗️ Erst planen

Die letzte erlaubte x-Position ist 780, die letzte erlaubte y-Position 580. Bei x = 800 oder y = 600 liegt der Kopf ausserhalb. Links und oben sind Werte kleiner als 0 ausserhalb.

## 🤖 Prompt 5

```text
Fressen und Wachsen funktionieren.
Wir verwenden weiterhin Python und Pygame Zero.

Jetzt benötigen wir Game Over.

Das Spiel endet, wenn:

1. der Kopf den linken oder rechten Spielfeldrand verlässt
2. der Kopf den oberen oder unteren Spielfeldrand verlässt
3. der Kopf den eigenen Körper berührt

Bei Game Over:

- Snake stoppt
- gross "GAME OVER" anzeigen

Baue die Prüfung möglichst einfach und verständlich auf.
Vergleiche den Kopf nicht mit sich selbst.
Beachte: Bei einem Schritt ohne Futter wird das letzte Segment frei.
Der Kopf darf auf dieses gerade frei werdende Feld ziehen.

Erkläre mir danach die Bedingungen, die zu Game Over führen.
```

## ▶️ Checkpoint

Starte für jeden Wandtest die Datei neu. Friss für den Selbstkollisionstest zuerst mehrere Futter und steuere dann in deinen Körper.

- [ ] Wandkollision funktioniert an allen vier Seiten.
- [ ] Selbstkollision funktioniert.
- [ ] Snake stoppt und bleibt auch bei Tastendrücken stehen.
- [ ] GAME OVER erscheint gut sichtbar.

## 🧠 Das kenne ich schon

In [Verzweigungen – if / elif / else](../mini-games/05-verzweigungen.md) hast du Bedingungen geprüft. Hier gilt zum Beispiel: **Wenn** der Kopf ausserhalb des Spielfelds liegt, wird Game Over gesetzt.

Zeige die Bedingungen für Wand und Körper im Code. Erkläre, warum der Kopf beim Vergleich mit dem Körper nicht mitgezählt wird.

[Zurück](04-wachsen.md) · [Zur Übersicht](index.md) · [Weiter: Punkte und Neustart](06-punkte-neustart.md)
