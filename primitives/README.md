# primitives

A component belongs here only if it appears on **more than one surface**.
Every primitive must:

1. read every colour, size and radius from `../tokens.css` — **zero hex literals**;
2. declare its surface (`paper` / `glass` / `both`) in a comment at the top;
3. add any new contrast pair it relies on to `../check_contrast.py`.

## The reference is the artifact

These are **derived from the canonical artifact** — the Three Meters calculator
build — not invented from this list. Where a primitive and the artifact disagree,
the artifact is right and the primitive is a bug. `label.css` and `readout.css`
are the two type voices and the two things most likely to drift; follow their
shape.

## The set

| File | Surface | Job |
|---|---|---|
| `label.css` | both | the label voice — names a thing |
| `readout.css` | glass | the readout voice — reports a quantity |
| `button.css` | both | the action. **UI voice at 14px, sentence case** — not the label voice |
| `seg.css` | paper | segmented control — how a closed question is asked |
| `field.css` | paper | an open question — label, control, and where the figure came from |
| `card.css` | paper | a raised surface; plain / settled / unconfirmed |
| `chip.css` | glass | an inline figure, inset into a paper layout |
| `status-badge.css` | both | names a state or provenance; never a quantity |
| `meter.css` | glass | a quantity as a bar; `--gauge` adds marks and a wall |
| `band.css` | glass | the shared shell of every glass zone — full bleed + inner rail |
| `marquee.css` | glass | zone 1 · where you are. Sticky, flush to the top |
| `screen.css` | glass | zone 3 · the figures, and the figure grid |
| `base.css` | glass | zone 4 · the one action |

## Three things that are easy to get wrong

**A button is not a label.** Uppercase, letterspaced, 10px is for *naming* a
thing. Asking someone to *do* something is 14px sentence case. Getting this
backwards makes every call to action look like a caption.

**Nor is a field's label.** Same trap, same fix: `.field > label` is the UI
voice at 14px sentence case, because a person reads it with their hands on the
keyboard. `.label` belongs on the kicker *above* a group of fields — the thing
that names the group — never on the questions inside it.

**A zone is not a box.** `band` / `marquee` / `screen` / `base` are full-bleed
page furniture: the glass runs edge to edge and the *content* is centred on
`--rail`. They carry no radius, no border around the zone, and no outer margin —
"the glass is inset, never floating" is a statement about the page, not a
description of a card.
