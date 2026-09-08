# Anbindung an OpenSpec

OpenSpec legt unter `openspec/` ab:

```
openspec/
├── project.md                 # oft fehlend oder veraltet → spec-lens pflegt sie
├── specs/<capability>/spec.md # Source of Truth, eine Datei pro Capability
└── changes/
    ├── <change-name>/
    │   ├── proposal.md        # warum, was ändert sich
    │   ├── design.md          # technischer Ansatz
    │   ├── tasks.md           # Implementierungs-Checkliste (ignorieren)
    │   └── specs/<capability>/spec.md  # Delta: ADDED / MODIFIED / REMOVED
    └── archive/<datum>-<change-name>/
```

Vorher prüfen, ob die Struktur in diesem Projekt abweicht (`ls openspec/`).

## Was pro Zelle gelesen wird

| Zelle | Quellen |
|---|---|
| Fachlich · System | alle `specs/*/spec.md` (nur Überschriften + Requirement-Titel), `proposal.md` des Changes |
| Fachlich · Teil | `changes/<name>/specs/*/spec.md` (Deltas) plus die zugehörigen Ist-Specs |
| Architekt · System | `project.md` (falls vorhanden), `design.md`, alle Capability-Namen |
| Architekt · Teil | `design.md`, Deltas, Ist-Specs der betroffenen Capabilities |

`tasks.md` nie lesen – reine Implementierungsdetails.

## Betroffenen Teil ableiten

1. Capabilities, für die ein Delta unter `changes/<name>/specs/` liegt → Kern.
2. Capabilities, die in `design.md` oder `proposal.md` namentlich vorkommen
   → Nachbarn (`rand`).
3. Alles andere ignorieren.

## project.md pflegen

`project.md` wird von spec-lens **generiert**, nie von Hand geschrieben.
Inhalt = Zelle "Architekt · Gesamtsystem" im Ist-Zustand (ohne Vorher/Nachher):

- Zweck des Projekts in 3 Sätzen
- Capability-Liste mit je einem Satz
- Komponentendiagramm (flowchart mit Schichten)
- Hauptdatenflüsse (max. 3)
- Bekannte Tradeoffs

Trigger zum Neu-Generieren: nach jedem `/opsx:archive` bzw. `openspec archive`,
oder manuell mit `/spec-lens projekt --persp architekt --zoom system --write`.
Kopfzeile der Datei: `<!-- generiert von spec-lens am <datum>, nicht manuell editieren -->`.

## Rückfluss der Antworten

Wenn der Nutzer Approval-Fragen beantwortet und `--write` gesetzt ist:
Antworten als Abschnitt `## Review (spec-lens, <datum>)` an `proposal.md`
anhängen. Kein Umschreiben der Spec – das bleibt Aufgabe des normalen
OpenSpec-Workflows.
