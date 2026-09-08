#!/usr/bin/env bash
# spec-lens installieren/aktualisieren für Claude Code und pi.
#
#   ./install.sh                 global: ~/.agents/skills + Symlink ~/.claude/skills  (einmalig, gilt für alle Repos)
#   ./install.sh --project       ins aktuelle Repo: .agents/skills + Symlink .claude/skills (zum Committen)
#   ./install.sh --update        git pull auf der globalen Installation
#   SPEC_LENS_REPO=<git-url> ./install.sh   Quelle aus Git statt aus diesem Ordner
set -euo pipefail
NAME=spec-lens
SRC="$(cd "$(dirname "$0")" && pwd)"
MODE="${1:-global}"

link() { mkdir -p "$(dirname "$2")"; rm -rf "$2"; ln -s "$1" "$2"; echo "  link  $2 -> $1"; }

case "$MODE" in
  --update|update)
    T="$HOME/.agents/skills/$NAME"
    if [ -d "$T/.git" ]; then git -C "$T" pull --ff-only; echo "aktualisiert: $T"
    else echo "Keine Git-Installation unter $T. Neu installieren mit SPEC_LENS_REPO=<url> ./install.sh"; exit 1; fi ;;
  --project|project)
    ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
    T="$ROOT/.agents/skills/$NAME"
    mkdir -p "$(dirname "$T")"; rm -rf "$T"; cp -r "$SRC" "$T"; rm -rf "$T/.git"
    echo "  copy  $T"
    link "../../.agents/skills/$NAME" "$ROOT/.claude/skills/$NAME"
    echo "Fertig. .agents/ und .claude/skills/ committen." ;;
  global|--global)
    T="$HOME/.agents/skills/$NAME"
    mkdir -p "$(dirname "$T")"
    if [ -n "${SPEC_LENS_REPO:-}" ]; then
      rm -rf "$T"; git clone --quiet "$SPEC_LENS_REPO" "$T"; echo "  clone $T"
    else
      rm -rf "$T"; cp -r "$SRC" "$T"; echo "  copy  $T"
    fi
    link "$T" "$HOME/.claude/skills/$NAME"
    echo "Fertig. Gilt für alle Repos. In pi /reload, in Claude Code neue Session." ;;
  *) echo "Unbekannter Modus: $MODE"; sed -n '2,8p' "$0"; exit 1 ;;
esac
