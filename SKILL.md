---
name: spec-lens
description: Übersetzt umfangreiche Specs, OpenSpec-Changes und Architektur-Dokumente in kurze, bewertbare Zusammenfassungen mit einfachen Mermaid-Diagrammen (Anforderungsliste, Fallbeschreibungen, Vorher/Nachher-Diagramm, Risiken, Approval-Fragen). Immer verwenden, wenn der Nutzer eine Spec, ein Feature, einen Change oder ein Projekt "bewerten", "einordnen", "reviewen", "zusammenfassen", "verstehen" oder "freigeben" will, wenn er fragt "was ändert sich durch X", "wie wirkt sich X aus", "zeig mir den Fluss/Prozess/die Architektur", oder wenn ein openspec/-Verzeichnis im Projekt liegt. Auch verwenden, wenn der Nutzer sagt, dass ihm eine Spec zu lang oder zu technisch ist.
---

# spec-lens

Translation-Layer zwischen Spec und Mensch. Der Mensch liest keine Specs, er
beantwortet Approval-Fragen zu einer einseitigen Zusammenfassung mit Diagramm.

## Grundprinzip

Zwei unabhängige Achsen bestimmen den Scope. Der Nutzer wählt die Perspektive,
der Ausschnitt wird aus dem Feature abgeleitet.

| | Gesamtsystem | Betroffener Teil |
|---|---|---|
| **Fachlich** | Welche Prozesse/Anforderungen ändern sich im Projekt? | Wie ändert sich der Ablauf im betroffenen Prozess? |
| **Architekt** | Wie ändert sich der Kommunikationsfluss insgesamt? | Wie ändert sich der Fluss zwischen betroffenen Komponenten? |

Alle vier Zellen nutzen dasselbe Template (siehe unten). Unterschiede sind nur
Vokabular und Diagrammtyp.

## Aufruf

```
/spec-lens <ziel> [--persp fachlich|architekt] [--zoom system|teil] [--fokus <name>]
```

- `<ziel>`: Change-Name, Capability, Datei oder "projekt"
- Default: `--persp fachlich --zoom system`
- `--fokus`: manuelles Überschreiben des abgeleiteten Ausschnitts
- Fehlt ein Parameter, ansagen welcher Default gilt – nicht nachfragen.
- Der Aufruf ist eine Konvention, kein Parser: auch "bewerte den Change X aus
  Architektensicht" ist ein gültiger Aufruf. Parameter aus dem Satz ableiten.

## Ablauf

1. **Quellen einsammeln.** Bei OpenSpec-Projekten: `references/openspec.md`
   lesen, dort steht, welche Dateien pro Zelle relevant sind. Sonst die
   angegebene Spec plus direkt referenzierte Dokumente.
2. **Betroffenen Teil ableiten** (nur bei `--zoom teil`): Alle Prozesse bzw.
   Komponenten, die in Spec-Deltas (ADDED/MODIFIED/REMOVED), design.md oder
   proposal.md genannt werden. Nachbarn, die nur berührt werden, kommen als
   graue Boxen mit Einzeiler an den Rand.
3. **Template füllen.** Passende Zelle aus `references/templates.md` nehmen.
4. **Diagramm bauen** nach `references/diagrams.md`. Genau ein Diagramm pro
   Zelle, immer Vorher/Nachher wenn ein Change bewertet wird.
5. **Approval-Fragen stellen** – 3 bis 5, jede mit Ja/Nein beantwortbar.
6. Antworten des Nutzers als Kommentar in die Change-Dateien zurückschreiben
   (nur wenn der Nutzer das will).

## Ausgabeort

Ergebnis immer als Datei schreiben, zusätzlich im Chat anzeigen:
`openspec/reviews/<ziel>--<persp>--<zoom>.md` (bzw. `docs/reviews/` ohne OpenSpec).
Grund: Mermaid rendert nicht im Terminal, aber in VS Code, GitHub und Obsidian.
Existiert die Datei, überschreiben – Reviews sind Momentaufnahmen, kein Log.

Nach dem Schreiben immer `python3 <skill-dir>/scripts/render.py <datei>` ausführen:
erzeugt eine `.html` daneben und öffnet sie im Browser, wo die Diagramme
gerendert werden. Im Chat nur die Kurzfassung und die Approval-Fragen wiederholen,
nicht das Diagramm.

## Harte Regeln

- Ausgabe pro Zelle: max. 1 Bildschirmseite Text + 1 Diagramm.
- Anforderungen: max. 7 Stichpunkte. Fälle: max. 3. Risiken: max. 5.
- Keine Implementierungsdetails: keine Signaturen, keine Dateinamen, keine
  Bibliotheken, kein Code. Schnittstellen nur als "wer redet mit wem, worüber".
- Jede Annahme, die nicht in der Spec steht, mit `⚠ Annahme:` markieren.
- Bei echter Unklarheit: eine Frage stellen, nicht raten.
- Immer nennen, was **unberührt** bleibt. Das ist die halbe Bewertungsgrundlage.
- Diagramme nur in Mermaid. Kein Bild, kein externes Tool.

## Ausgabe-Template (gilt für alle vier Zellen)

```
# <Ziel> · <Perspektive> · <Zoom>

## Kurzfassung (3 Sätze)
## Anforderungen (max. 7)
## Fälle (max. 3, je: Auslöser → Verhalten → Ergebnis)
## Diagramm (Vorher/Nachher oder Ist)
## Was sich ändert / Was unberührt bleibt
## Risiken & Tradeoffs (max. 5)
## ⚠ Annahmen
## Approval-Fragen (3–5, Ja/Nein)
```

Vollständiges Beispiel: `assets/beispiel.md`.

## Weiterführende Dateien

- `references/templates.md` – die vier Zellen im Detail
- `references/diagrams.md` – welcher Mermaid-Diagrammtyp wofür, Konventionen
- `references/openspec.md` – Mapping auf OpenSpec-Verzeichnisstruktur, project.md
- `assets/beispiel.md` – Referenzausgabe (Change, architekt, teil)
- `scripts/render.py` – Markdown+Mermaid → HTML, öffnet Browser
