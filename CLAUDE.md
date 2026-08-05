# graphr-tokens — notes for Claude Code

**This package is the source of truth for every visual decision across Graphr.**
Changes here propagate to the hub, every tool, and every app. Treat edits as
breaking until proven otherwise.

Canonical human source: `Bob Style Guide v2.0-C Cabinet (standalone).html`
in `Documents/Claude-Work/About me/`. This package is its machine form.

## Before you commit anything that touches colour

```
python3 check_contrast.py     # must print PROBLEMS: 0
```

It checks every foreground/background pair against the guide's measured §03
table and against the 4.5:1 AA floor. It also asserts that the **banned** pairs
still fail — if a "banned" pair starts passing, someone changed a token and the
rule that depends on it is now wrong.

## Do not

- **Do not read `bob-design-language.md`** in the `About me/` folder for colour.
  It documents **v2.0** — two papers and violet `#52277F`. This project is
  **v2.0-C** — one paper and spruce `#3D6B64`. There is no violet in this system.
- **Do not add a colour.** The palette is closed. If you need an in-between,
  derive it in oklch from spruce / clay / phosphor and add it here with a
  contrast entry — never inline in a consuming repo.
- **Do not add a shadow, a gradient, or a radius above 4px.** Hairlines, hard
  edges and the glass do the containing. The rounded floating card is retired.
- **Do not duplicate these values** into a consuming repo. They are consumed as
  a git dependency precisely so they cannot drift.

## The rules the tokens encode

**Cream speaks. Glass reports.** One paper (`--cream`), one glass (`--screen`).
Sentences and serif live on paper; figures, counts and live states live on glass,
inset into the paper, never floating on it. Nothing crosses: no serif prose on
glass, no phosphor on paper.

**The cabinet is the layout.** Four zones, in this order, always: glass
**marquee** (where you are) · cream **body** (you read and act here) · glass
**screen** (the figures) · glass **base** (the one action). A view with two
screens has no discipline; a view with none is missing the signature.

**Surface-locked colours.** `--phosphor` / `--phosphor-dim` are glass-only.
`--spruce` is paper-only (≈3:1 on glass — a smudge). `--clay` never carries
light text at any size; every fill at UI size is `--clay-deep`.

**One accent acts.** `--clay-deep` — fills, links, urgent labels, kickers. Same
hex on both surfaces. `--spruce` is structure and label ground, **never a button**.

**Two type voices with floors.** Label voice: Figtree 700, UPPERCASE, 10px
minimum, 0.14–0.22em. Readout voice: system mono, tabular, 10px minimum, glass
only, and only ever for a *quantity*. Neither goes below 10px — at these
letter-spacings that is the edge of legibility and it is the first thing to drift.

**Banned:** `#6366F1` and any bright teal-cyan (the category defaults this system
exists to leave) · gradients · emoji · soft shadows · pixel fonts, sprites,
points, confetti, levels.

## Adding a primitive

A primitive belongs here only if it appears on more than one surface. It must:

1. read every colour, size and radius from `tokens.css` — zero hex literals;
2. state which surface it is for (paper / glass / both) in a comment at the top;
3. ship with the contrast pair it relies on added to `check_contrast.py`.

Current set: `button` · `card` · `status-badge` · `meter` · `readout` · `label` ·
`marquee` · `screen` · `base`.

## Two known errata in the source guide

§03 has two wrong numbers, **both in the FAILS column** — where the exact value
carries no weight, which is presumably why they drifted:

| Pair | Guide says | Measured |
|---|---|---|
| spruce on glass | 2.3:1 | **2.95:1** |
| phosphor-dim on cream | 1.8:1 | **1.67:1** |

Both fail AA either way, so every rule that depends on them is unchanged and
correct. `check_contrast.py` carries the measured values. **Do not "correct"
them back to the guide's numbers** — the script is right; the guide has typos.

All 18 other pairs verify exactly.
