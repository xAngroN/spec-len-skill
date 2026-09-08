# Installation – Claude Code und pi

Beide lesen dasselbe Format (Agent-Skills-Standard). Ein Ordner reicht.

## Einmalig global (empfohlen – gilt dann in jedem Repo)
```
./install.sh
```
Legt `~/.agents/skills/spec-lens` an (pi liest das nativ) und einen Symlink
`~/.claude/skills/spec-lens` (Claude Code).

## Per Git pflegen und updaten
Skill-Ordner in ein eigenes Repo legen, dann:
```
SPEC_LENS_REPO=git@github.com:<du>/spec-lens.git ./install.sh   # einmal
./install.sh --update                                            # später
```
Update = `git pull`. Änderungen am Skill machst du im Repo, nicht in `~/.agents`.

## Ins Team-Repo committen
Im Zielrepo:
```
~/.agents/skills/spec-lens/install.sh --project
```
Kopiert nach `.agents/skills/spec-lens` + Symlink `.claude/skills/spec-lens`. Beides committen.
Update im Projekt: Befehl erneut ausführen (überschreibt).

## Alternative ohne Symlink
pi auf den Claude-Code-Ordner zeigen lassen – in `.pi/settings.json`:
```json
{ "skills": ["../.claude/skills"] }
```

## Aufruf
- Claude Code: `/spec-lens add-dark-mode --persp architekt --zoom teil`
- pi: `/skill:spec-lens` oder natürlich: „bewerte add-dark-mode aus Architektensicht, nur betroffener Teil"
- Nach Änderungen an SKILL.md: pi `/reload`, Claude Code neue Session.

## Ergebnis ansehen
Terminals rendern kein Mermaid. Der Skill schreibt `openspec/reviews/<ziel>--<persp>--<zoom>.md`
und ruft `scripts/render.py` auf → `.html` daneben, öffnet sich im Browser. Kein Install nötig.
Alternativ: `.md` in VS Code mit Extension "Markdown Preview Mermaid Support" (Strg+Shift+V).
