# 🎮 Schritt 2 – Bewegung und Steuerung

## Ziel · ca. 25 Minuten

Snake bewegt sich automatisch und lässt sich mit den Pfeiltasten steuern.

## 🏗️ Erst planen

Der Kopf rückt jeweils eine Rasterzelle weiter. Der Körper folgt. Überlege: Welche Koordinate verändert sich bei einer Bewegung nach rechts?

## 🤖 Prompt 2

```text
Die Schlange wird korrekt angezeigt.

Jetzt soll sie sich bewegen und mit den Pfeiltasten gesteuert werden.
Wir verwenden weiterhin Python und Pygame Zero.

Anforderungen:

- Bewegung immer genau 20 Pixel
- Startbewegung nach rechts
- Pfeiltasten für oben, unten, links, rechts
- eine Variable speichert die aktuelle Richtung
- keine direkte 180-Grad-Drehung
- höchstens eine Richtungsänderung pro Bewegungsschritt zulassen,
  damit auch schnelle Tastendrücke keine Umkehr ermöglichen
- Bewegung soll regelmässig erfolgen und nicht von der Bildrate abhängen
- verwende dafür die Pygame-Zero-Uhr clock.schedule_interval:
  ein Bewegungsschritt alle 0.2 Sekunden
- noch kein Futter
- die Schlange behält ihre Länge von 3 Segmenten

Verändere nur das, was für diesen Schritt notwendig ist.

Erkläre mir danach:

1. Wie bewegt sich die Schlange?
2. Warum darf sie sich nicht direkt um 180 Grad drehen?
3. Welche Variable speichert die Richtung?
```

## ▶️ Checkpoint

Speichere und starte das Spiel neu. Klicke ins Spielfenster, damit es Tastendrücke erhält.

- [ ] Snake bewegt sich automatisch nach rechts.
- [ ] Alle vier Pfeiltasten funktionieren.
- [ ] Snake bewegt sich in 20-Pixel-Schritten und bleibt drei Segmente lang.
- [ ] Eine direkte Umkehr ist nicht möglich: Bei Bewegung nach rechts wird links ignoriert.
- [ ] Auch sehr schnelle Tastendrücke ermöglichen keine direkte Umkehr.

Steuere frühzeitig um die Ecke. **Wände prüfen wir erst in Schritt 5.** Falls Snake aus dem Fenster läuft, schliesse das Spiel und starte es neu.

## 🧠 Verstehen

Lass dir im Code zeigen, wo ein neuer Kopf eingefügt und das letzte Segment entfernt wird. Die Zeit zwischen zwei Bewegungsschritten steuert das Tempo; die Bildrate beschreibt, wie oft das Fenster neu gezeichnet wird.

> **🏗️ Architekten-Frage:** Was müsste man verändern, damit Snake schneller läuft?
>
> Zeige die zuständige Zahl im Code und erkläre, ob sie grösser oder kleiner werden müsste.

[Zurück](01-start.md) · [Zur Übersicht](index.md) · [Weiter: Futter](03-futter.md)
