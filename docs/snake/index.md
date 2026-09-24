# 🐍 Snake mit KI entwickeln

Wir bauen gemeinsam ein Snake-Spiel mit Python und **Pygame Zero**.

Diesmal programmiert die KI einen grossen Teil des Codes für uns. Aber: Die KI entscheidet nicht, wie unser Spiel aussehen soll. Wir sind die Architekt:innen.

> **ICH entscheide WAS.**  
> **Die KI hilft beim WIE.**  
> **ICH teste, ob es funktioniert.**

Bei den **Mini-Games** war die KI dein Tutor: **ICH programmiere → KI erklärt**.

Bei **Snake** bestimmst du als Architekt:in die Regeln: **ICH plane → KI programmiert → ICH teste → ICH verbessere**.

## 🔄 So arbeiten wir

1. 🏗️ **PLANEN** – Was soll als Nächstes funktionieren?
2. 🤖 **PROMPT** – Wir beschreiben der KI möglichst genau den Auftrag.
3. 💻 **CODE** – Die KI erstellt oder verändert den Code.
4. ▶️ **TESTEN** – Wir starten das Spiel.
5. 🧠 **VERSTEHEN** – Wir schauen uns an, was verändert wurde.
6. 🔧 **VERBESSERN** – Erst danach kommt der nächste Schritt.

> **Nie fünf neue Funktionen gleichzeitig bauen. Kleine Schritte – oft testen.**

## Unser Weg zum Spiel

Für das gemeinsame Grundspiel planen wir **ungefähr 2 Stunden**, inklusive Tests und kurzen Erklärungen. Python, VS Code und Pygame Zero sollten vorher bereit sein.

| Schritt | Das bauen wir | Zeit |
| --- | --- | --- |
| [1 – Spielfeld + Schlange](01-start.md) | Unser erster Prototyp | 20 Min. |
| [2 – Bewegung + Steuerung](02-bewegung.md) | Bewegung mit Pfeiltasten | 25 Min. |
| [3 – Futter](03-futter.md) | Zufälliges Futter auf dem Raster | 15 Min. |
| [4 – Fressen + Wachsen](04-wachsen.md) | Die Schlange wird länger | 20 Min. |
| [5 – Kollision + Game Over](05-game-over.md) | Wände und Körper prüfen | 20 Min. |
| [6 – Punkte + Neustart](06-punkte-neustart.md) | Das Grundspiel abschliessen | 20 Min. |
| [7 – Mein eigenes Snake](07-mein-snake.md) | Deine eigene Erweiterung | zusätzlich 30–45 Min. |

## So arbeitest du mit dem Code

1. Verwende für alle Schritte dieselbe Datei `snake.py` und möglichst denselben KI-Chat.
2. Gib der KI immer deinen **aktuellen Code**, falls sie ihn nicht sehen kann. Wir bleiben in allen Schritten bei **Python und Pygame Zero**.
3. Lies den Auftrag und sende den Prompt. Übernimm die Änderungen, speichere die Datei und starte das Spiel neu.
4. Teste den Checkpoint. Lass dir die Änderung kurz erklären und zeige die passende Stelle im Code.
5. Sichere vor dem nächsten Schritt eine funktionierende Kopie, zum Beispiel `snake_schritt1.py`.

Wenn etwas nicht funktioniert, beschreibe: **Was habe ich getan? Was habe ich erwartet? Was ist passiert?** Kopiere eine Fehlermeldung vollständig in den Chat. Bitte die KI, zuerst diesen Fehler zu beheben.

## ▶️ Checkpoint

- [ ] Ich kann erklären, wer WAS und wer WIE entscheidet.
- [ ] Ich weiss: Erst testen und verstehen, dann weiterbauen.

[Los geht’s: Spielfeld und Snake](01-start.md)
