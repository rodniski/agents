"""Generate the README hero (assets/hero-{light,dark}.svg).

    python3 assets/build.py

Stdlib only. One folder on the left, the three harnesses on the right, and
the symlinks between them drawn once in sequence. Every line and label is
visible in the base styles; the animation only draws strokes that are
already there, so a renderer that ignores CSS animation shows the full map.
"""

from pathlib import Path

OUT = Path(__file__).resolve().parent

# Same tokens as the humanizing README, so the two repos read as one family.
THEMES = {
    "light": dict(bg="#fbfaf7", border="#e4e1da", ink="#1c1b19", muted="#8a857c",
                  instr="#2f6f5e", skills="#b4442a"),
    "dark": dict(bg="#151514", border="#2c2b28", ink="#ecebe6", muted="#8f8b82",
                 instr="#6fc2a8", skills="#e2805f"),
}
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"

W, H = 880, 440
SRC = dict(x=48, y=137, w=272, h=170)
INSTR_OUT = (SRC["x"] + SRC["w"], SRC["y"] + 64)
SKILLS_OUT = (SRC["x"] + SRC["w"], SRC["y"] + 124)

# name, instructions path, skills path (None = harness has no skills link)
HARNESSES = [
    ("Claude Code", "~/.claude/CLAUDE.md", "~/.claude/skills"),
    ("Codex", "~/.codex/AGENTS.md", None),
    ("Cursor", "rules/gui-agents.mdc", "~/.cursor/skills"),
]
BOX = dict(x=520, w=312, h=92, y0=64, gap=20)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def curve(a, b):
    """Horizontal S-curve from a to b, plus its approximate length."""
    (x1, y1), (x2, y2) = a, b
    mx = (x1 + x2) / 2
    pts = [(x1, y1), (mx, y1), (mx, y2), (x2, y2)]
    length, prev = 0.0, pts[0]
    for i in range(1, 41):
        t = i / 40
        x = sum(c * p[0] for c, p in zip(((1 - t) ** 3, 3 * t * (1 - t) ** 2, 3 * t * t * (1 - t), t ** 3), pts))
        y = sum(c * p[1] for c, p in zip(((1 - t) ** 3, 3 * t * (1 - t) ** 2, 3 * t * t * (1 - t), t ** 3), pts))
        length += ((x - prev[0]) ** 2 + (y - prev[1]) ** 2) ** 0.5
        prev = (x, y)
    d = f"M{x1},{y1} C{mx},{y1} {mx},{y2} {x2},{y2}"
    return d, round(length) + 2


def hero(t):
    links, boxes, delay = [], [], 0.4
    for i, (name, instr, skills) in enumerate(HARNESSES):
        y = BOX["y0"] + i * (BOX["h"] + BOX["gap"])
        x = BOX["x"]
        boxes.append(
            f'<rect class="box" x="{x}" y="{y}" width="{BOX["w"]}" height="{BOX["h"]}" rx="10"/>'
            f'<text x="{x + 20}" y="{y + 30}" class="name">{esc(name)}</text>'
            f'<text x="{x + 20}" y="{y + 56}" class="path instr">{esc(instr)}</text>'
            f'<text x="{x + 20}" y="{y + 78}" class="path {"skills" if skills else "none"}">'
            f'{esc(skills or "no skills link")}</text>'
        )
        for out, target_y, cls, present in ((INSTR_OUT, y + 51, "instr", True),
                                            (SKILLS_OUT, y + 73, "skills", bool(skills))):
            if not present:
                continue
            d, length = curve(out, (x - 6, target_y))
            links.append(
                f'<path class="link {cls}" d="{d}" style="stroke-dasharray:{length};'
                f'animation-delay:{delay:.2f}s;--len:{length}"/>'
                f'<circle class="end {cls}" cx="{x - 6}" cy="{target_y}" r="3.5" '
                f'style="animation-delay:{delay + 0.45:.2f}s"/>'
            )
            delay += 0.35

    css = f"""
    .card{{fill:{t['bg']};stroke:{t['border']}}}
    .box{{fill:none;stroke:{t['border']}}}
    .src{{fill:none;stroke:{t['muted']};stroke-dasharray:4 4}}
    .cap{{font:600 12.5px {SANS};letter-spacing:.12em;fill:{t['muted']}}}
    .name{{font:600 17px {SANS};fill:{t['ink']}}}
    .file{{font:600 18px {MONO};fill:{t['ink']}}}
    .note{{font:14px {SANS};fill:{t['muted']}}}
    .path{{font:14px {MONO}}}
    .instr{{fill:{t['instr']};stroke:{t['instr']}}}
    .skills{{fill:{t['skills']};stroke:{t['skills']}}}
    .none{{fill:{t['muted']}}}
    text.instr,text.skills{{stroke:none}}
    .link{{fill:none;stroke-width:1.6;stroke-dashoffset:0;animation:draw .5s ease-out backwards}}
    .end{{stroke:none;animation:pop .25s ease-out backwards}}
    .foot{{font:14px {SANS};fill:{t['muted']}}}
    @keyframes draw{{from{{stroke-dashoffset:var(--len)}}}}
    @keyframes pop{{from{{opacity:0}}}}
    @media (prefers-reduced-motion: reduce){{*{{animation:none!important}}}}
    """
    sx, sy, sw, sh = SRC["x"], SRC["y"], SRC["w"], SRC["h"]
    return "\n".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
        f'aria-label="One folder, ~/.agents, linked by symlinks to Claude Code, Codex and Cursor: '
        f'AGENTS.md as instructions for all three, skills/ for Claude Code and Cursor.">',
        f"<style>{css}</style>",
        f'<rect class="card" x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="14"/>',
        f'<text x="{sx}" y="{BOX["y0"] - 22}" class="cap">ONE FOLDER</text>',
        f'<text x="{BOX["x"]}" y="{BOX["y0"] - 22}" class="cap">THREE HARNESSES</text>',
        f'<rect class="src" x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="10"/>',
        f'<text x="{sx + 22}" y="{sy + 36}" class="path none">~/.agents</text>',
        f'<text x="{sx + 22}" y="{INSTR_OUT[1] + 6}" class="file">AGENTS.md</text>',
        f'<text x="{sx + 22}" y="{INSTR_OUT[1] + 28}" class="note">instructions, always on</text>',
        f'<text x="{sx + 22}" y="{SKILLS_OUT[1] + 6}" class="file">skills/</text>',
        f'<text x="{sx + 22}" y="{SKILLS_OUT[1] + 28}" class="note">40 skills, flat symlinks</text>',
        f'<circle class="end instr" cx="{INSTR_OUT[0]}" cy="{INSTR_OUT[1]}" r="3.5"/>',
        f'<circle class="end skills" cx="{SKILLS_OUT[0]}" cy="{SKILLS_OUT[1]}" r="3.5"/>',
        *links,
        *boxes,
        f'<text x="{sx}" y="{H - 34}" class="foot">bin/ensure-redirects creates every link. Nothing is copied.</text>',
        "</svg>",
    ])


if __name__ == "__main__":
    for name, t in THEMES.items():
        (OUT / f"hero-{name}.svg").write_text(hero(t))
    print("wrote", sorted(p.name for p in OUT.glob("hero-*.svg")))
