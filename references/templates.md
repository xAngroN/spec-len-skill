# Die vier Zellen

Gemeinsames Grundgerüst steht in SKILL.md. Hier nur, was pro Zelle anders ist.

## 1. Fachlich · Gesamtsystem

Frage: Welche Prozesse und Anforderungen des Projekts ändern sich?

- Anforderungen: nur die, die neu sind oder sich ändern. Bestehende werden
  gezählt, nicht aufgelistet ("12 unverändert").
- Fälle: End-to-End aus Nutzersicht, kein technisches Vokabular.
- Diagramm: Prozesslandkarte (`flowchart`), Prozesse als Boxen, geänderte
  Prozesse markiert.
- Typische Approval-Fragen: "Ist Prozess X wirklich betroffen?", "Fehlt ein
  Prozess?", "Ist die Nicht-Zielsetzung Y richtig?"

## 2. Fachlich · Betroffener Teil

Frage: Wie ändert sich der Ablauf innerhalb des betroffenen Prozesses?

- Anforderungen: nur die dieses Prozesses, inkl. Regeln und Ausnahmen.
- Fälle: Hauptfall, ein Fehlerfall, ein Randfall.
- Diagramm: Ablaufdiagramm mit Swimlanes (BPMN-Näherung via `flowchart` +
  `subgraph` pro Rolle). Vorher/Nachher als zwei Diagramme oder farblich
  markiert.
- Typische Approval-Fragen: "Ist Schritt 3 so gewollt?", "Wer entscheidet bei
  Ausnahme Z?", "Darf Schritt 5 übersprungen werden?"

## 3. Architekt · Gesamtsystem

Frage: Wie ändert sich der Kommunikationsfluss des Projekts?

- Anforderungen: nicht-funktional (Last, Verfügbarkeit, Sicherheit), nur die
  betroffenen.
- Fälle: ersetzt durch "Hauptdatenflüsse" (max. 3).
- Diagramm: Komponentenübersicht (`flowchart` oder `C4Context`), Schichten
  als `subgraph`, neue/geänderte Verbindungen markiert.
- Typische Approval-Fragen: "Neue Abhängigkeit A→B akzeptabel?", "Gehört die
  Logik in Schicht X?", "Erhöht das die Kopplung unzulässig?"

## 4. Architekt · Betroffener Teil

Frage: Wie ändert sich der Fluss zwischen den betroffenen Komponenten?

- Anforderungen: Schnittstellenverträge in Prosa ("liefert Liste von
  Bestellungen mit Status") plus Datenmodell-Änderungen falls vorhanden.
- Fälle: ersetzt durch Hauptfall als Sequenz.
- Diagramm: `sequenceDiagram` für den Hauptfall; bei Datenmodell-Änderung
  zusätzlich `erDiagram` (Ausnahme von der Ein-Diagramm-Regel).
- Typische Approval-Fragen: "Synchron oder asynchron richtig?", "Wer ist
  Owner der neuen Entität?", "Fehlerfall bei Schritt 4 abgedeckt?"

## Vorher/Nachher-Konvention

Bei Changes immer beide Zustände zeigen. Kürzeste Form: ein Diagramm, in dem
Neues mit `:::neu`, Entfalltes mit `:::weg`, Geändertes mit `:::mod` markiert
ist. Wenn das unleserlich wird, zwei getrennte Diagramme untereinander.
