# 6. Testen, dokumentieren und kreativ weiterbauen

## Wann ist deine Änderung fertig?

«Es startet» ist erst der erste Test. Prüfe zusätzlich das gewünschte Verhalten, einen Grenzfall und eine bisher funktionierende Funktion. Zum Beispiel: neue Farbe am Rand, alle vier Ränder, anschliessend Neustart und Schliessen.

## Mein Lernprotokoll

Erstelle `lernprotokoll.md` im Spielordner. Du kannst die folgende Vorlage kopieren; sie liegt auch unter `beispiele/snake/lernprotokoll.md`.

```markdown
# Meine KI-Änderung

- Ziel und Datei:
- Meine Vermutung:
- Mein Prompt:
- Übernommener oder verworfener Vorschlag und Begründung:
- Eine geänderte Codezeile in meinen eigenen Worten:

| Situation | Erwartung | Beobachtung | Bestanden? |
| --- | --- | --- | --- |
| Normalfall | | | |
| Grenzfall | | | |
| Bisherige Funktion | | | |

- Das verstehe ich jetzt:
- Hier brauche ich noch Hilfe:
```

## Kreativauftrag

Wähle **eine** Erweiterung. Speichere deine Version unter `snake_eigen.py`. Schreibe vor dem KI-Prompt zwei Sätze zum Ziel und drei erwartete Testergebnisse auf.

| Idee | Schwierigkeit | Beispiel für einen Test |
| --- | --- | --- |
| Eigene Farben und Fenstertitel | Leicht | Kopf und Futter bleiben unterscheidbar |
| Kopf anders färben als Körper | Leicht | Farbe bleibt nach dem Wachsen richtig |
| Tempo nach jeweils fünf Punkten erhöhen | Mittel | Änderung erst bei 5, 10, 15 Punkten |
| Pause mit P | Mittel | Schlange steht; P setzt fort; Esc funktioniert weiterhin |
| Hindernisse | Anspruchsvoll | Futter und Startkörper liegen nicht im Hindernis |

Die Grundlösung enthält diese Erweiterungen nicht. Lass die KI nicht gleichzeitig Menü, Musik, Grafik und neue Regeln ändern. Teste nach jedem kleinen Schritt.

## Partnerprüfung

Eine Person spielt, die andere beobachtet. Tauscht danach die Rollen. Beantwortet gemeinsam:

1. Entspricht das Verhalten dem Auftrag?
2. Kann die Person ihre Änderung erklären?
3. Welche Tests wurden wirklich durchgeführt?
4. Was hat die KI beigetragen, was wurde selbst entschieden?

## Ausblick: Snake Advanced

Im Kursprojekt liegt unter `beispiele/Snake_Advanced` eine umfangreichere Version mit zusätzlichen Spielideen. Die `README.md` erklärt Start und Bedienung. Nutze sie nach dem einfachen Snake als Inspiration: Suche dir ein Merkmal aus und beschreibe zuerst, wie du es in deinem eigenen Spiel testen würdest.

Eine kleine, verstandene und geprüfte Erweiterung ist ein vollständiges Unterrichtsergebnis. Du musst nicht den gesamten Advanced-Code nachbauen.

[Zurück zur Übersicht](index.md)
