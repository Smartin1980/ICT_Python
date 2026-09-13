# Achtung, Hai! – Pygame-Zero-Lehrerversion

Mit diesem Programm können Befehlsfolgen der Schülerinnen und Schüler direkt
eingegeben und auf dem Spielbrett animiert werden.

## Installation

1. Python installieren.
2. In VS Code oder einer Eingabeaufforderung im Spielordner `beispiele/Achtung_Hai` ausführen:

   ```bash
   python -m pip install pgzero
   ```

3. Das Spiel starten:

   ```bash
   pgzrun main.py
   ```

   Falls `pgzrun` nicht gefunden wird:

   ```bash
   python -m pgzero main.py
   ```

## Bedienung

- Name anklicken und eingeben.
- Befehlsfolge anklicken und eingeben, zum Beispiel `V V L V V`.
- Auf **START** klicken.
- Jede Sekunde wird genau ein Befehl ausgeführt.
- **ZURÜCKSETZEN** setzt das Boot wieder auf das Startfeld.

Erlaubte Befehle:

- `V`: ein Feld vorwärts
- `R`: 90 Grad nach rechts drehen
- `L`: 90 Grad nach links drehen

Auch Folgen ohne Leerzeichen wie `VVLVV` funktionieren.

## Spielregeln der digitalen Version

- Das Boot startet unten in der Mitte und blickt nach Norden.
- Die nummerierten Bootsfelder 1–4 sind die vier möglichen Ziele/Stege.
- Ein Haifeld beendet die Fahrt.
- Holzstege und der Spielfeldrand dürfen nicht befahren werden.
- Die ausgeführte Route wird mit kleinen Markierungen angezeigt.

## Anpassungen für den Unterricht

Im oberen Teil von `achtung_hai.py` lassen sich die Felder ändern. `main.py` ist der Einstiegspunkt zum Starten des Spiels:

```python
START = (6, 3)
SHARKS = {...}
DOCKS = {...}
GOALS = {...}
```

Die Koordinaten werden als `(Zeile, Spalte)` notiert und beginnen bei `0`.
Die Ausführungsgeschwindigkeit steht ebenfalls in `achtung_hai.py`, in `start_run()` und
`execute_next_command()` bei `1.0` Sekunden.
