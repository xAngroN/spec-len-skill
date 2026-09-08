#!/usr/bin/env python3
"""Rendert eine Markdown-Datei mit Mermaid-Blöcken als HTML und öffnet sie im Browser.
Aufruf: python3 scripts/render.py openspec/reviews/foo.md [--no-open]
Nur Python-Standardbibliothek, Mermaid kommt per CDN."""
import re, sys, html, pathlib, subprocess, platform

src = pathlib.Path(sys.argv[1])
open_browser = "--no-open" not in sys.argv
md = src.read_text(encoding="utf-8")

def block(m):
    return f'<pre class="mermaid">{html.escape(m.group(1))}</pre>'
body = re.sub(r"```mermaid\n(.*?)```", block, md, flags=re.S)
# minimale Markdown-Umsetzung: Überschriften, Listen, Absätze
out = []
for line in body.splitlines():
    if line.startswith("<pre") or line.startswith("</pre") or (out and out[-1].startswith("<pre") and "</pre>" not in out[-1]):
        out.append(line); continue
    if m := re.match(r"^(#{1,6}) (.*)", line):
        out.append(f"<h{len(m[1])}>{html.escape(m[2])}</h{len(m[1])}>")
    elif m := re.match(r"^(\d+)\. (.*)", line):
        out.append(f"<li>{html.escape(m[2])}</li>")
    elif line.startswith("- "):
        out.append(f"<li>{html.escape(line[2:])}</li>")
    elif line.strip():
        out.append(f"<p>{html.escape(line)}</p>")
doc = f"""<!doctype html><meta charset="utf-8"><title>{html.escape(src.stem)}</title>
<style>body{{font:15px/1.5 system-ui;max-width:900px;margin:2rem auto;padding:0 1rem}}
li{{margin-left:1.2rem}}pre.mermaid{{background:#fafafa;padding:1rem;border-radius:6px}}</style>
<script type="module">import m from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";m.initialize({{startOnLoad:true}});</script>
{chr(10).join(out)}"""
dst = src.with_suffix(".html")
dst.write_text(doc, encoding="utf-8")
print(dst)
if open_browser:
    cmd = {"Darwin": ["open"], "Windows": ["cmd", "/c", "start", ""]}.get(platform.system(), ["xdg-open"])
    try: subprocess.Popen(cmd + [str(dst)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e: print("Browser nicht geöffnet:", e)
