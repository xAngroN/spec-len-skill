# Installation – Claude Code und pi

Beide lesen dasselbe Format (Agent-Skills-Standard). Ein Ordner reicht.

## Empfohlen: ein Ort, beide Tools

Projektweit:
```
mkdir -p .agents/skills
cp -r spec-lens .agents/skills/
ln -s ../../.agents/skills/spec-lens .claude/skills/spec-lens   # für Claude Code
```
pi findet `.agents/skills/` von selbst. Claude Code über den Symlink in `.claude/skills/`.

Global:
```
cp -r spec-lens ~/.agents/skills/
ln -s ~/.agents/skills/spec-lens ~/.claude/skills/spec-lens
```

## Alternative ohne Symlink
pi auf den Claude-Code-Ordner zeigen lassen – in `.pi/settings.json`:
```json
{ "skills": ["../.claude/skills"] }
```

## Aufruf
- Claude Code: `/spec-lens add-dark-mode --persp architekt --zoom teil`
- pi: `/skill:spec-lens` oder einfach natürlich: „bewerte add-dark-mode aus Architektensicht, nur betroffener Teil"
- Nach Änderungen an SKILL.md in pi `/reload`, in Claude Code neue Session.

## Ergebnis ansehen
Der Skill schreibt nach `openspec/reviews/<ziel>--<persp>--<zoom>.md`.
Datei in VS Code (Markdown-Vorschau) oder auf GitHub öffnen – dort rendert Mermaid.
