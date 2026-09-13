# 1. KI verstehen und sinnvoll fragen

## Lernziel

Du kannst erklären, warum KI-Code geprüft werden muss, und einen klaren Auftrag für eine kleine Änderung formulieren.

## Was macht ein Sprachmodell?

Ein Sprachmodell hat beim Training Muster aus vielen Beispielen gelernt. Es erzeugt seine Antwort schrittweise anhand deines Auftrags und des verfügbaren Kontexts. So kann es auch Python-Code erklären oder vorschlagen. Eine plausibel klingende Antwort ist aber noch kein Beweis, dass der Code deine Aufgabe erfüllt.

Im einfachen Browser-Chat sieht die KI deinen lokalen VS-Code-Ordner nicht automatisch. Teile den relevanten Code und die genaue Fehlermeldung als Text. Behauptet eine Antwort «funktioniert», kontrolliere das durch eigene Tests auf deinem Computer.

## Drei hilfreiche Rollen

| Rolle | Beispielauftrag |
| --- | --- |
| Erklären | «Erkläre, warum y beim Bewegen nach oben kleiner wird.» |
| Hinweise geben | «Gib mir einen Tipp für die Randprüfung, noch keine Lösung.» |
| Prüfen helfen | «Welche Grenzfälle fehlen in meinen Tests?» |

## Unsere Regeln

- Teile nur den benötigten Übungscode. Keine Namenlisten, Passwörter, Schlüssel oder privaten Daten; persönliche Angaben in Dateipfaden entfernst du aus Fehlermeldungen.
- Lass dir unbekannte Befehle erklären, bevor du sie ausführst. Für dieses Projekt ist nur Pygame als Zusatzpaket vorgesehen.
- Übernimm eine kleine Änderung nach der anderen und sichere vorher den funktionierenden Stand.
- Erkläre den übernommenen Code und notiere, wobei die KI geholfen hat.
- Nutze nur einen für den Unterricht freigegebenen Zugang. Wenn du keinen hast, arbeitest du mit den vorbereiteten Hinweisen; Zugangsdaten werden nicht geteilt.

## Ein guter Prompt hat fünf Teile

**Ziel + Vorwissen + aktueller Code + Grenzen + gewünschte Hilfe.**

Unklar wäre: «Mach mir Snake.» Präziser ist:

```text
Ich lerne Python und kenne Variablen, Listen, if/else, Schleifen und Funktionen.
Ich baue ein einfaches Snake mit Pygame, ohne Bilder oder weitere Bibliotheken.
Mein Kopf soll sich auf einem Raster bewegen und am Fensterrand stehen bleiben.
Gib zuerst einen Hinweis und eine Denkfrage. Noch keinen vollständigen Code.
Behalte meine Variablennamen bei. Hier ist mein aktueller Code:
[Hier meinen Code einfügen]
```

Die eckige Platzhalterzeile ersetzt du durch deinen Code. Wenn die Antwort zu kompliziert ist: «Erkläre diesen Vorschlag mit meinen bisherigen Python-Grundlagen. Zeige nur die nötige Änderung.»

## Erst überlegen

- Warum kann korrekter Python-Code trotzdem das falsche Spiel ergeben?
- Was musst du der KI zeigen, damit sie deinen Fehler untersuchen kann?
- Woran erkennst du, dass eine Änderung funktioniert?

## Übung: Eine überzeugende, aber falsche Antwort

Ein **absichtlich fehlerhafter, vorbereiteter Vorschlag** behauptet: «Damit bleibt der Kopf im Spielfeld.» Dies ist ein Ausschnitt, kein vollständiges Programm:

```python
if x <= SPALTEN:
    x = x + 1
```

Das Raster hat 24 Spalten mit den Nummern 0 bis 23. Rechne auf Papier mit `x = 23`: Welcher neue Wert entsteht? Was fehlt für die anderen Richtungen?

## Lösung zum Vergleichen

Bei 23 ist die Bedingung wahr; der Kopf landet bei 24 ausserhalb des Rasters. Prüfe die **nächste** Position für beide Achsen: `0 <= neu_x < SPALTEN` und `0 <= neu_y < ZEILEN`. Erst wenn beide Bedingungen gelten, übernimmst du die neue Position. Eine gut formulierte Erklärung ersetzt diesen Test nicht.

[Weiter: Umgebung einrichten](02-setup.md)
