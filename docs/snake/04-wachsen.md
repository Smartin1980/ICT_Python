# 🍎➡️🐍 Schritt 4 – Fressen und wachsen

## Ziel · ca. 20 Minuten

Snake frisst Futter und wächst dabei um genau ein Segment.

## 🏗️ Erst planen

Wir vergleichen die Position des Kopfes mit der Futterposition. Sind beide gleich, ist das Futter gefressen.

## 🤖 Prompt 4

```text
Jetzt soll Snake das Futter fressen können.
Wir verwenden weiterhin Python und Pygame Zero.

Wenn der Kopf dieselbe Position wie das Futter erreicht:

- Futter gilt als gefressen
- Snake wird um ein Segment länger
- neues Futter erscheint zufällig

Wenn kein Futter gefressen wird:

- Snake behält dieselbe Länge

Das neue Futter darf nicht auf Snake erscheinen.

Verändere nur den notwendigen Code.

Erkläre mir danach:

Warum entfernen wir bei einer normalen Bewegung das letzte Segment
der Schlange, beim Fressen aber nicht?
```

## ▶️ Checkpoint

Friss ein Futter und zähle die Segmente. Wiederhole den Test mit einem zweiten Futter.

- [ ] Futter verschwindet beim Fressen.
- [ ] Neues Futter erscheint auf einer freien Rasterzelle.
- [ ] Snake wächst um genau ein Segment: von 3 auf 4, dann auf 5.
- [ ] Ohne weiteres Futter bleibt die Länge gleich.

## 🧠 Der zentrale Lernpunkt

> **Warum entfernen wir bei einer normalen Bewegung das letzte Segment der Schlange, beim Fressen aber nicht?**
>
> Erkläre es zuerst selbst mit drei gezeichneten Quadraten. Zeige danach die beiden Fälle im Code.

Bei jedem Schritt kommt vorne ein neuer Kopf dazu. Entfernen wir hinten ein Segment, bleibt die Länge gleich. Beim Fressen bleibt das hinterste Segment erhalten: Die Liste hat jetzt einen Eintrag mehr.

[Zurück](03-futter.md) · [Zur Übersicht](index.md) · [Weiter: Game Over](05-game-over.md)
