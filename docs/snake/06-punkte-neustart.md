# 🏆 Schritt 6 – Punkte und Neustart

## Ziel · ca. 20 Minuten

Dies ist der letzte Schritt des gemeinsamen Grundspiels. Wir zählen Punkte und starten nach Game Over mit der Leertaste neu.

## 🏗️ Erst planen

Überlege vor dem Prompt: Welche Werte müssen wieder so sein wie beim ersten Start?

## 🤖 Prompt 6

```text
Unser Snake funktioniert.
Wir verwenden weiterhin Python und Pygame Zero.

Jetzt fehlen Punkte und Neustart.

Punkte:

- Variable score
- Startwert 0
- jedes Futter +1 Punkt
- Score oben links anzeigen
- bei Game Over sichtbar lassen

Neustart:

Wenn Game Over ist, soll die Leertaste ein neues Spiel starten.
Während des laufenden Spiels löst die Leertaste keinen Neustart aus.

Beim Neustart:

- Snake wieder 3 Segmente an der Startposition
- Startrichtung rechts
- Score = 0
- neues Futter auf einer freien Rasterzelle
- Game Over zurücksetzen
- auch die Sperre für Richtungsänderungen zurücksetzen

Erstelle dafür eine Funktion:

reset_game()

Verwende sie auch beim ersten Spielstart.
Die Bewegung darf nach mehreren Neustarts nicht schneller werden.
Plane den Bewegungstakt mit clock.schedule_interval nur einmal ein.

Halte den Code einfach.

Erkläre mir danach:

1. Wo wird score initialisiert?
2. Wo wird score verändert?
3. Wo wird score angezeigt?
4. Warum ist reset_game() eine Funktion?
```

## ▶️ Checkpoint

Friss zwei Futter, löse Game Over aus und drücke die Leertaste. Wiederhole den Neustart mehrmals.

- [ ] Punkte funktionieren: 0 beim Start, 1 nach einem Futter, 2 nach zwei Futtern.
- [ ] Game Over funktioniert weiterhin und der Score bleibt sichtbar.
- [ ] Die Leertaste startet nach Game Over neu, während des Spiels aber nicht.
- [ ] Snake beginnt wieder mit drei Segmenten und bewegt sich nach rechts.
- [ ] Score beginnt wieder bei 0 und neues Futter liegt auf einer freien Zelle.
- [ ] Steuerung und Tempo stimmen auch nach mehreren Neustarts.

## 🧠 Das kenne ich schon

Eine [Funktion](../mini-games/08-funktionen.md) bündelt einen Auftrag. `reset_game()` setzt die Startwerte an einer Stelle zurück. Zeige im Code, wo die Funktion beim ersten Start und beim Neustart aufgerufen wird.

> # 🎉 Unser Snake funktioniert!
>
> Wir haben jetzt ein vollständiges Grundspiel.
>
> ✓ Bewegung  
> ✓ Steuerung  
> ✓ Futter  
> ✓ Wachsen  
> ✓ Kollision  
> ✓ Punkte  
> ✓ Neustart

Sichere jetzt eine Kopie deines funktionierenden Grundspiels. Danach entscheidest du, wie dein Snake weitergeht.

[Zurück](05-game-over.md) · [Zur Übersicht](index.md) · [Weiter: Mein Snake](07-mein-snake.md)
